import pytest

from my_bot.main import main


def test_main_prints_message(capsys: pytest.CaptureFixture[str]) -> None:
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello from my-bot!\n"
