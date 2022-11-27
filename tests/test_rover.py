from src.rover import Rover
import pytest

@pytest.mark.parametrize("direction, expected",
    [ 
        ("N", [1,0]),
        ("E", [0,1]),
        ("S", [-1,0]),
        ("W", [0,-1]),
        ("w", [0,-1]),
    ]
)

def test_init_sucess(direction, expected):
    rover = Rover(game_map=[5,5], start_location=[0,0], start_direction=direction)
    
    assert rover.direction == expected

@pytest.mark.parametrize("game_map, start_location, direction, expected", 
    [ 
        ([4,2], [1,1], "G", "Start direction 'G' is not valid, please use N, E, S, or W"),
        ([3,1], [1,1], "4","Start direction '4' is not valid, please use N, E, S, or W"),
        ([3,3], [5,5], "N","Start location must be inside map area"),
        ([0,0], [1,1], "N","Map must be created with non zero, positive values"),
        ([-1,1], [1,1], "N","Map must be created with non zero, positive values"),
    ]
)

def test_init_fails(capsys, game_map, start_location, direction, expected):
    with pytest.raises(SystemExit):
        Rover(game_map=game_map, start_location=start_location, start_direction=direction)
    
    result_stderr = capsys.readouterr().err

    assert result_stderr == expected


@pytest.mark.parametrize("direction, move, end_location",
    [ 
        ("N", "FFFF", [4, 0]),
        ("E", "FFF", [0, 3]),
    ]
)

def test_movement(direction, move, end_location):
    # Arrange
    rover = Rover(game_map=[5,5], start_location=[0,0], start_direction=direction)

    # Act
    rover.move(move)

    # Assert

    assert rover.location == end_location

@pytest.mark.parametrize("direction, move, end_location",
    [ 
        ("S", "FFFF", [0, 0]),
        ("W", "FFF", [0, 0]),
        ("N", "FFFFFF", [5, 0]),
        ("E", "FFFFFF", [0, 5]),
        ("E", "FFFFFFLLFFF", [0, 5]),
    ]
)

def test_crash(direction, move, end_location):
    # Arrange
    rover = Rover(game_map=[5,5], start_location=[0,0], start_direction=direction)

    # Act
    rover.move(move)

    # Assert

    assert rover.location == end_location


@pytest.mark.parametrize("direction, move, end_direction",
    [ 
        ("S", "L", [0,1]),
        ("W", "R", [1,0]),
        ("N", "LL", [-1,0]),
        ("E", "RR", [0,-1]),
        ("N", "LLR", [0,-1]),
        ("W", "RRL", [1,0]),
        ("E", "RRRRRR", [0,-1]),
        ("N", "LLLLLL", [-1,0]),
    ]
)

def test_rotate(direction, move, end_direction):
    # Arrange
    rover = Rover(game_map=[5,5], start_location=[0,0], start_direction=direction)

    # Act
    rover.move(move)

    # Assert

    assert rover.direction == end_direction

@pytest.mark.parametrize('direction, move',
    [ 
        ("S", "U"),
        ("E", "FFB"),
    ]
)

def test_invalid_move(capsys, direction, move):
    # Arrange
    rover = Rover(game_map=[5,5], start_location=[0,0], start_direction=direction)

    # Act

    with pytest.raises(SystemExit):
        rover.move(move)

    # Assert
    result_stderr = capsys.readouterr().err
    expected = "Invalid Move!"

    assert result_stderr == expected
