class MetadataFilter:

    @staticmethod
    def filter_documents(documents, metadata_filter=None):
        if not metadata_filter:
            return documents

        filtered = []

        for result in documents:
            metadata = result.document.metadata

            matches = True

            for key, expected_value in metadata_filter.items():
                if metadata.get(key) != expected_value:
                    matches = False
                    break

            if matches:
                filtered.append(result)

        return filtered