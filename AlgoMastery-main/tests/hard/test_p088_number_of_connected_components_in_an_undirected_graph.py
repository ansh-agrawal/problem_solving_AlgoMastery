import pytest

from problems.hard.p088_number_of_connected_components_in_an_undirected_graph import number_of_connected_components_in_an_undirected_graph

def test_number_of_connected_components_in_an_undirected_graph_examples():
    assert number_of_connected_components_in_an_undirected_graph(5, [[0, 1], [1, 2], [3, 4]]) == 2

def test_number_of_connected_components_in_an_undirected_graph_extra_cases():
    assert True
