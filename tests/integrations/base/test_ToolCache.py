import os
import platform
import shutil
import sys
from pathlib import Path

import pytest
import requests
from cookiecutter.main import cookiecutter

from briefcase.console import Console, Log
from briefcase.integrations.base import ToolCache


@pytest.fixture
def simple_tools(tmp_path):
    return ToolCache(
        logger=Log(),
        console=Console(),
        base_path=tmp_path,
    )


def test_toolcache_typing():
    """Tool typing for ToolCache is correct."""
    expected_type_defs = {
        "android_sdk": "AndroidSDK",
        "docker": "Docker",
        "download": "Download",
        "flatpak": "Flatpak",
        "java": "JDK",
        "linuxdeploy": "LinuxDeploy",
        "rcedit": "RCEdit",
        "subprocess": "Subprocess",
        "visualstudio": "VisualStudio",
        "wix": "WiX",
        "xcode": "bool",
        "xcode_cli": "bool",
    }
    for tool_name, tool_type in expected_type_defs.items():
        assert ToolCache.__annotations__[tool_name] == tool_type

    assert "DockerAppContext" in ToolCache.__annotations__["app_context"]
    assert "Subprocess" in ToolCache.__annotations__["app_context"]


def test_third_party_tools_available():
    """Third party tools are available."""
    assert ToolCache.os is os
    assert ToolCache.platform is platform
    assert ToolCache.shutil is shutil
    assert ToolCache.sys is sys

    assert ToolCache.cookiecutter is cookiecutter
    assert ToolCache.requests is requests


def test_always_true(simple_tools, tmp_path):
    """Implicit boolean casts are always True."""
    assert simple_tools or False
    simple_tools["app-1"].app_context = "tool"
    assert simple_tools["app-1"] or False


def test_mapping_protocol(simple_tools):
    """ToolCache is a mapping."""
    simple_tools["app-1"].tool = "tool 1"
    simple_tools["app-2"].tool = "tool 2"

    assert [app for app in simple_tools] == ["app-1", "app-2"]
    assert len(simple_tools) == 2
    assert simple_tools["app-1"].tool == "tool 1"
    assert simple_tools["app-2"].tool == "tool 2"


def test_host_arch_and_os(simple_tools):
    """Arch and OS represent host arch and OS."""
    assert simple_tools.host_arch == platform.machine()
    assert simple_tools.host_os == platform.system()


def test_base_path_is_path(simple_tools):
    """Base path is always a Path."""
    # The BaseCommand tests have much more extensive tests for this path.
    assert isinstance(simple_tools.base_path, Path)
    tools = ToolCache(
        logger=Log(),
        console=Console(),
        base_path="/home/data",
    )
    assert isinstance(tools.base_path, Path)


def test_home_path_default(simple_tools):
    """Home path default is current user's home directory."""
    assert simple_tools.home_path == Path.home()


@pytest.mark.skipif(platform.system() == "Windows", reason="Linux/macOS specific tests")
@pytest.mark.parametrize(
    "home_path, expected_path",
    [
        (None, Path.home()),
        ("/path/to/home", Path("/path/to/home")),
        ("~", Path.home()),
        ("~/dir", Path.home() / "dir"),
    ],
)
def test_nonwindows_home_path(home_path, expected_path, tmp_path):
    """Home path is always expanded or defaulted."""
    tools = ToolCache(
        logger=Log(),
        console=Console(),
        base_path=tmp_path,
        home_path=home_path,
    )
    assert tools.home_path == expected_path


@pytest.mark.skipif(platform.system() != "Windows", reason="Windows specific tests")
@pytest.mark.parametrize(
    "home_path, expected_path",
    [
        (None, Path.home()),
        ("Y:\\path\\to\\home", Path("Y:\\path\\to\\home")),
        ("~", Path.home()),
        ("~/dir", Path.home() / "dir"),
    ],
)
def test_windows_home_path(home_path, expected_path, tmp_path):
    """Home path is always expanded or defaulted."""
    tools = ToolCache(
        logger=Log(),
        console=Console(),
        base_path=tmp_path,
        home_path=home_path,
    )
    assert tools.home_path == expected_path


def test_add_tool():
    """Added tools are returned and available via attribute."""
    tools = ToolCache(
        logger=Log(),
        console=Console(),
        base_path="/home/data",
    )
    tool_name = "toolname"
    tool = object()

    assert tools.add_tool(name=tool_name, tool=tool) is tool
    assert getattr(tools, tool_name) is tool
