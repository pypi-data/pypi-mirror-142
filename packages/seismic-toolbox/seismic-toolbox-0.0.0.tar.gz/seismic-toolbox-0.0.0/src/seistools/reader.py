"""
Provides an inteface to read seismic data written in binary files with a basic
structure of: File header, trace header0, trace0, trace header 1 , trace 1 etc..
All the boilerm plate functions are provided in the SegReader interface.
An open source implementation for a SEGY version 1 is provided, with a ctypes function
to convert IBM32 floats to IEEE.

# MIT License
# Copyright(c) 2017 Olivier Winter
# https: // en.wikipedia.org / wiki / MIT_License
"""

import abc
import ctypes
import logging
import os
from pathlib import Path
import struct

import numpy as np

logger = logging.getLogger(__name__)


def bcd2dec(bcd):
    """
    :param bcd: np.array of uint8
    :return:
    """
    bcd = np.array([bcd]) if np.isscalar(bcd) else bcd
    decode = np.floor(bcd / 16) * 10 + np.mod(bcd, 16)
    decode[np.mod(bcd, 16) > 9] = np.nan
    decode = np.sum(decode * 100 ** np.flipud(np.arange(bcd.size)))
    return decode


def _load_ibm2float_shared_library():
    # Try to locate the .so file in the same directory as this file
    if os.name == 'nt':
        _file = 'sampleconversion.dll'
    else:
        _file = 'sampleconversion.x86_64.so'
    library_path = Path(__file__).parent.joinpath(_file)
    return ctypes.cdll.LoadLibrary(library_path)


class SegReader(abc.ABC):
    """
    Base Seg Reader class.
    Applicable for files containing a file header, and fixed trace headers and trace length
    The resulting variable is indexable as would be a numpy array
    """

    def __init__(self, file_path):
        """
        Should label properties
        self.sample_size
        self.thsize  # binary trace header size in bytes
        self.fhsize  # binary file header size in bytes
        self.ns
        self.fh  # file header structure
        self.fhbin  # binary file header
        self.n_bytes_file  # total file length in bytes
        self.ns  # number of samples per trace
        self.ntr  # number of traces
        self.rl  # record length (s)
        self.si  # sampling interval (s)
        self.thsize  # single binary trace header size in bytes
        self.sample_size = 4
        self.sample_format = np.dtype
        :return:
        """
        self.file = Path(file_path)
        self.n_bytes_file = self.file.stat().st_size
        self.read_fh()

    def __str__(self):
        str = f"SegReader object (ntr, ns) {(self.ntr, self.ns)} sampled at {self.si * 1e3}ms"
        return str

    @property
    def sample_size(self):
        return np.dtype(self.sample_dtype).type().nbytes

    @abc.abstractmethod
    def read_fh(self):
        """
        :return: dictionary
        """
        pass

    def interpret_data(self, samplebin):
        """
        from a binary array of uint8, interpret samples with endianess and
        sample conversions
        :return: array of size [ntr, ns]
        """
        return samplebin.view(self.sample_dtype)

    @abc.abstractmethod
    def interpret_thbin(thbin):
        """
        from an array of
        :return: dictionary of numpy arrays of size [ntr, ...]
        """
        pass

    def read(self, first=0, last=None):
        """
        Reads and interpret the seismic data for a subselection of traces
        :param first: first trace to read (0-based indexing) (defaults to 0)
        :param last:  last trace to read (0-based indexing) (defaults to self.ntr)
        :return: np.array (ntr, ns) and dictionary of np.arrays as trace header
        """
        last = last or self.ntr
        ntr2read = last - first
        nbytes_per_trace = int(self.ns * self.sample_size + self.thsize)
        offset = first * (self.ns * self.sample_size + self.thsize) + self.fhsize
        with self.file.open('rb') as fid:
            fid.seek(offset)
            data = np.fromfile(fid, dtype='uint8', count=nbytes_per_trace * ntr2read)
            data = data.reshape(ntr2read, nbytes_per_trace)
        # dissociate the trace header from the trace data
        thbin, data = np.split(data, [self.thsize], 1)
        # pack the arrays for optimized contiguous access
        thbin = np.ascontiguousarray(thbin)
        data = np.ascontiguousarray(data)
        data = self.interpret_data(data)
        th = self.interpret_thbin(thbin)
        return data, th


class SegyReader(SegReader):
    """
    SegyReader class for segd v1
    sr = SegyReader(segy_file)
    """
    # tech debt: implement loadsheets for file and trace headers
    fhsize = 3600
    thsize = 240
    _mod_ctype = _load_ibm2float_shared_library()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def ibm2ieee_float(self, w):
        pt = w.ctypes.data_as(ctypes.POINTER(ctypes.c_int32))
        self._mod_ctype.ibm_to_float(pt, pt, w.size, 0)
        w = w.view(np.float32)
        return w

    def read_fh(self):
        """
        sets properties
        self.fh
        self.ntr
        self.ns
        self.si
        :return:
        """
        with self.file.open('rb') as fid:
            self.fhbin = fid.read(self.fhsize)
        ebcdic = self.fhbin[:3200]
        fhbin = self.fhbin[3200:]
        fh = {}
        # Interpret EBDCIC
        fh['text_head'] = ebcdic.decode('EBCDIC-CP-BE')
        # Parse binary file header
        fh['task'] = struct.unpack('>i', fhbin[0:4])[0]
        fh['line'] = struct.unpack('>i', fhbin[4:8])[0]
        fh['data_trace_per_ensemble'] = struct.unpack('>h', fhbin[12:14])[0]
        fh['auxiliary_trace_per_ensemble'] = struct.unpack('>h', fhbin[14:16])[0]
        fh['si'] = struct.unpack('>h', fhbin[16:18])[0]
        fh['si_orig'] = struct.unpack('>h', fhbin[18:20])[0]
        fh['ns'] = struct.unpack('>H', fhbin[20:22])[0]
        fh['ns_orig'] = struct.unpack('>H', fhbin[22:24])[0]
        fh['data_sample_format'] = struct.unpack('>h', fhbin[24:26])[0]
        fh['ensemble_fold'] = struct.unpack('>h', fhbin[26:28])[0]
        fh['trace_sorting'] = struct.unpack('>h', fhbin[28:30])[0]
        fh['measurement_system'] = struct.unpack('>h', fhbin[54:56])[0]
        fh['segy_format_revision_number'] = struct.unpack('>h', fhbin[300:302])[0]
        # after having read the file header, populates the reader properties
        self.fh = fh
        self.si = fh['si'] / 1e6
        # get the samplesize in bytes (almost always 4 but...)
        self.ns = self.fh['ns']
        # compute number of traces
        self.sample_dtype = ['>I', '>i', '>h', '', '>f'][self.fh['data_sample_format'] - 1]
        self.ntr = int((self.n_bytes_file - self.fhsize) / (self.thsize + self.ns * self.sample_size))

    def interpret_data(self, samplebin):
        if self.fh['data_sample_format'] == 1:
            return self.ibm2ieee_float(samplebin)
        else:
            return samplebin.view(self.sample_dtype)

    @staticmethod
    def interpret_thbin(thbin):
        format_tuple = (  # (str_name, str_format, first, nbytes)
            ('ffid', '>i', 8, 4),
            ('trace_number', '>i', 12, 4),
            ('cdp', '>i', 20, 4),
            ('trace_id', '>h', 28, 2),
            ('vertical_stack', '>h', 30, 2),
            ('horizonal_stack', '>h', 32, 2),
            ('offset', '>i', 36, 4),
            ('receiver_z', '>i', 40, 4),
            ('source_z', '>i', 44, 4),
            ('source_depth', '>i', 48, 4),
            ('receiver_datum_elevation', '>i', 52, 4),
            ('shot_datum_elevation', '>i', 56, 4),
            ('shot_water_depth', '>i', 60, 4),
            ('receiver_water_depth', '>i', 64, 4),
            ('elevation_scalar', '>h', 68, 2),
            ('coordinates_scalar', '>h', 70, 2),
            ('source_x', '>i', 72, 4),
            ('source_y', '>i', 76, 4),
            ('receiver_x', '>i', 80, 4),
            ('receiver_y', '>i', 84, 4),
            ('coordinates_units', '>h', 88, 2),
            ('year', '>h', 156, 2),
            ('julian_day', '>h', 158, 2),
            ('hour', '>h', 160, 2),
            ('minute', '>h', 162, 2),
            ('second', '>h', 164, 2),
            ('millisecond', '>h', 168, 2),
            ('cdp_x', '>i', 180, 4),
            ('cdp_y', '>i', 184, 4),
            ('inline', '>i', 188, 4),
            ('crossline', '>i', 192, 4),
            ('trace_value_measurement_unit', '>h', 202, 2),
        )
        th = {}
        for ft in format_tuple:
            str_name, str_format, offset, size = ft
            th[str_name] = np.copy(thbin[:, offset:(offset + size)]).view(str_format).squeeze()
        return th
