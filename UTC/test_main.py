#!/usr/bin/env python3
"""
Unit tests for the MockGitTest application.
"""

import unittest
import sys
import os

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'SRC'))

from main import MockGitTest


class TestMockGitTest(unittest.TestCase):
    """Test cases for MockGitTest class."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.app = MockGitTest()
    
    def test_init(self):
        """Test application initialization."""
        self.assertEqual(self.app.version, "1.0.0")
        self.assertEqual(self.app.name, "Mock Git Test")
    
    def test_get_info(self):
        """Test get_info method."""
        info = self.app.get_info()
        self.assertIsInstance(info, dict)
        self.assertEqual(info["name"], "Mock Git Test")
        self.assertEqual(info["version"], "1.0.0")
        self.assertIn("description", info)
    
    def test_process_data(self):
        """Test process_data method."""
        input_data = ["hello", "world", "test"]
        expected = ["HELLO", "WORLD", "TEST"]
        result = self.app.process_data(input_data)
        self.assertEqual(result, expected)
    
    def test_process_data_empty(self):
        """Test process_data with empty list."""
        result = self.app.process_data([])
        self.assertEqual(result, [])
    
    def test_process_data_with_empty_strings(self):
        """Test process_data with empty strings."""
        input_data = ["hello", "", "world", ""]
        expected = ["HELLO", "WORLD"]
        result = self.app.process_data(input_data)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
