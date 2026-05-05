import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(__file__))

from lab7 import bfs, build_graph, compute_max_flow, edmonds_karp, read_roads_csv


class TestBuildGraph(unittest.TestCase):

    def test_single_edge(self):
        graph = build_graph([("A", "B", 5)])
        self.assertEqual(graph["A"]["B"], 5)

    def test_reverse_edge_initialized(self):
        graph = build_graph([("A", "B", 5)])
        self.assertIn("A", graph["B"])

    def test_parallel_edges_summed(self):
        graph = build_graph([("A", "B", 3), ("A", "B", 7)])
        self.assertEqual(graph["A"]["B"], 10)

    def test_multiple_edges(self):
        edges = [("A", "B", 4), ("B", "C", 6), ("A", "C", 2)]
        graph = build_graph(edges)
        self.assertEqual(graph["A"]["B"], 4)
        self.assertEqual(graph["B"]["C"], 6)
        self.assertEqual(graph["A"]["C"], 2)


class TestBFS(unittest.TestCase):

    def test_path_exists(self):
        graph = build_graph([("S", "A", 5), ("A", "T", 3)])
        parent = {}
        self.assertTrue(bfs(graph, "S", "T", parent))
        self.assertIn("T", parent)

    def test_no_path(self):
        graph = build_graph([("S", "A", 5)])
        self.assertFalse(bfs(graph, "S", "T", {}))

    def test_zero_capacity_edge_ignored(self):
        graph = build_graph([("S", "A", 0), ("A", "T", 5)])
        self.assertFalse(bfs(graph, "S", "T", {}))

    def test_source_equals_sink(self):
        graph = build_graph([("A", "B", 5)])
        self.assertFalse(bfs(graph, "A", "A", {}))


class TestEdmondsKarp(unittest.TestCase):

    def test_simple_path(self):
        graph = build_graph([("S", "A", 5), ("A", "T", 5)])
        self.assertEqual(edmonds_karp(graph, "S", "T"), 5)

    def test_bottleneck(self):
        graph = build_graph([("S", "A", 10), ("A", "T", 3)])
        self.assertEqual(edmonds_karp(graph, "S", "T"), 3)

    def test_two_parallel_paths(self):
        edges = [("S", "A", 5), ("A", "T", 5), ("S", "B", 3), ("B", "T", 3)]
        self.assertEqual(edmonds_karp(build_graph(edges), "S", "T"), 8)

    def test_no_path(self):
        graph = build_graph([("S", "A", 5)])
        self.assertEqual(edmonds_karp(graph, "S", "T"), 0)

    def test_diamond_graph(self):
        edges = [("S", "A", 10), ("S", "B", 10), ("A", "T", 7), ("B", "T", 5)]
        self.assertEqual(edmonds_karp(build_graph(edges), "S", "T"), 12)

    def test_cross_paths(self):
        edges = [
            ("S", "A", 3), ("S", "B", 2),
            ("A", "B", 1), ("A", "T", 3),
            ("B", "T", 2),
        ]
        self.assertEqual(edmonds_karp(build_graph(edges), "S", "T"), 5)


class TestReadRoadsCSV(unittest.TestCase):

    @staticmethod
    def _write_csv(content):
        tmp = tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False, encoding="utf-8")
        tmp.write(content)
        tmp.close()
        return tmp.name

    def test_basic_parsing(self):
        path = self._write_csv("F1,F2\nS1,S2\nF1,X1,5\nX1,S1,3\n")
        farms, shops, edges = read_roads_csv(path)
        os.unlink(path)
        self.assertEqual(farms, ["F1", "F2"])
        self.assertEqual(shops, ["S1", "S2"])
        self.assertEqual(edges, [("F1", "X1", 5), ("X1", "S1", 3)])

    def test_invalid_edge_format(self):
        path = self._write_csv("F1\nS1\nF1,X1\n")
        with self.assertRaises(ValueError):
            read_roads_csv(path)
        os.unlink(path)

    def test_whitespace_handling(self):
        path = self._write_csv(" F1 , F2 \n S1 \n F1 , X1 , 7 \n")
        farms, shops, edges = read_roads_csv(path)
        os.unlink(path)
        self.assertEqual(farms, ["F1", "F2"])
        self.assertEqual(edges[0][2], 7)


class TestComputeMaxFlow(unittest.TestCase):

    @staticmethod
    def _write_csv(content):
        tmp = tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False, encoding="utf-8")
        tmp.write(content)
        tmp.close()
        return tmp.name

    def test_single_farm_single_shop(self):
        path = self._write_csv("F1\nS1\nF1,S1,8\n")
        result = compute_max_flow(path)
        os.unlink(path)
        self.assertEqual(result, 8)

    def test_multiple_farms_single_shop(self):
        path = self._write_csv("F1,F2\nS1\nF1,S1,5\nF2,S1,3\n")
        result = compute_max_flow(path)
        os.unlink(path)
        self.assertEqual(result, 8)

    def test_bottleneck_on_intermediate_node(self):
        path = self._write_csv("F1\nS1\nF1,X1,10\nX1,S1,4\n")
        result = compute_max_flow(path)
        os.unlink(path)
        self.assertEqual(result, 4)

    def test_no_connection(self):
        path = self._write_csv("F1\nS1\nF1,X1,10\n")
        result = compute_max_flow(path)
        os.unlink(path)
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()

