"""Specialized components for dataclass annotations."""

import marshmallow

from marshmallow_annotations.scheme import AnnotationSchema


class DataClassSchema(AnnotationSchema):
    """
    Derived class for creating dataclass instances with post-load conversino.
    """

    @marshmallow.post_load
    def make_instance(self, data):
        """Post load, deserialize to data class."""
        return self.opts.target(**data)
