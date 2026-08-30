"""
Metadata filtering for Week 4 Advanced RAG.

Supports filtering retrieved documents using metadata
such as source, page, and file type.
"""


class MetadataFilter:

    # Metadata fields supported by the Week 4 application.
    SUPPORTED_FIELDS = {
        "source",
        "page",
        "file_type",
    }

    @classmethod
    def validate(cls, filters: dict | None) -> dict | None:
        """
        Validate metadata filter fields.

        Example:
            {
                "source": "data\\documents\\Introduction to Database.pdf"
            }
        """

        if not filters:
            return None

        invalid_fields = set(filters.keys()) - cls.SUPPORTED_FIELDS

        if invalid_fields:
            raise ValueError(
                f"Unsupported metadata fields: {invalid_fields}. "
                f"Supported fields: {cls.SUPPORTED_FIELDS}"
            )

        return filters

    @staticmethod
    def matches(
        metadata: dict,
        filters: dict,
    ) -> bool:
        """
        Check whether a document's metadata matches
        all requested filters.
        """

        for key, expected_value in filters.items():

            actual_value = metadata.get(key)

            # Support multiple acceptable values.
            #
            # Example:
            # {
            #     "source": [
            #         "document1.pdf",
            #         "document2.pdf"
            #     ]
            # }
            if isinstance(expected_value, list):

                if actual_value not in expected_value:
                    return False

            else:

                if actual_value != expected_value:
                    return False

        return True