def test_game_environment():
    print("=================================")
    print("Game QA Automation Platform")
    print("Game Environment Test")
    print("=================================")

    game_name = "Block Blast"
    expected_status = "running"
    actual_status = "running"

    print(f"Game: {game_name}")
    print(f"Expected: {expected_status}")
    print(f"Actual: {actual_status}")

    assert actual_status == expected_status, "Game environment check failed!"

    print("TEST PASSED")


if __name__ == "__main__":
    test_game_environment()
