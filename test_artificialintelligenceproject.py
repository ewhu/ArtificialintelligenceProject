# test_artificialintelligenceproject.py
"""
Tests for ArtificialintelligenceProject module.
"""

import unittest
from artificialintelligenceproject import ArtificialintelligenceProject

class TestArtificialintelligenceProject(unittest.TestCase):
    """Test cases for ArtificialintelligenceProject class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ArtificialintelligenceProject()
        self.assertIsInstance(instance, ArtificialintelligenceProject)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ArtificialintelligenceProject()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
