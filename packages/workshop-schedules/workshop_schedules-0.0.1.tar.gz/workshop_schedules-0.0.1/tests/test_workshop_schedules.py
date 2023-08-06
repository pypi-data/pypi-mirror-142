#!/usr/bin/env python

"""Tests for `workshop_schedules` package."""

from click.testing import CliRunner

from workshop_schedules import cli


def test_version():
    import workshop_schedules

    assert workshop_schedules.__version__


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'workshop_schedules.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
