import src.search as search
from parameterized import parameterized

@parameterized.expand( 
    [ 
        (1,[],None),
        (1,[1],0),
        (2,[1],None),
        (1,[1, 2],0),
        (2,[1, 2],1),
        (3,[1, 2, 3],2),
        (1,[1, 2, 3, 4],0),
        (2,[1, 2, 3, 4],1),
        (3,[1, 2, 3, 4],2),
        (4,[1, 2, 3, 4],3),
        (1,[1, 2, 3, 4, 5],0),
        (2,[1, 2, 3, 4, 5],1),
        (3,[1, 2, 3, 4, 5],2),
        (4,[1, 2, 3, 4, 5],3),
        (5,[1, 2, 3, 4, 5],4),
        (99,[1, 2, 3, 4, 5],None),
    ]
)

def test_search_for_a_number_in_a_list(find, collection, expected):
    result = search.search(collection, find)
    assert result == expected
