from marshmallow import Schema, fields


class BaseSchema(Schema):
    """Base marshmallow schema with common attributes."""
    id = fields.String(dump_only=True)

    def load_object_into_schema(self, data, partial=False):
        """Helper function to load python objects into schema"""
        data, errors = self.load(data, partial=partial)

        if errors:
            print(errors)

        return data

    def dump_object_into_schema(self, data):
        """Helper function to dump python objects into schema"""
        data, errors = self.dump(data)

        if errors:
            print(errors)

        return data
