#!/usr/bin/env python3
"""Tests for the legacy dag module (backward compatibility)."""



class LegacyImportTestCase:
    """Verify the legacy dag module still imports."""

    def test_import_node_class(self):
        from dag.dag import Node
        assert Node is not None

    def test_import_link_class(self):
        from dag.dag import Link
        assert Link is not None
