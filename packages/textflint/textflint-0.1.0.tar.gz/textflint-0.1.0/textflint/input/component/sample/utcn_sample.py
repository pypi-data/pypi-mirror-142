"""
UT Sample Class
============================================

"""

from .cnsample import CnSample
from ..field import CnTextField

__all__ = ['UTCnSample']


class UTCnSample(CnSample):
    r""" Universal Transformation sample.

    Universe Transformation is not a subtask of NLP,
    implemented for providing universal text transformation function.

    """

    def __init__(
        self,
        data,
        origin=None,
        sample_id=None
    ):
        self.x = None
        super().__init__(data, origin=origin, sample_id=sample_id)

    def __repr__(self):
        return 'UTCnSample'

    def check_data(self, data):
        assert 'x' in data and isinstance(data['x'], str)

    def load(self, data):
        r"""
        Convert data dict which contains essential information to SASample.

        :param dict data: contains 'x' key at least.
        :return:

        """
        self.x = CnTextField(data['x'])

    def dump(self):
        return {'x': self.x.text, 'sample_id': self.sample_id}

    def is_legal(self):
        r"""
        Validate whether the sample is legal

        :return: bool

        """
        return True
