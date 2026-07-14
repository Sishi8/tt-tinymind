# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

"""
Temporary test for the seven-segment output mapping design.

The three lowest input bits select one dedicated output:

    ui_in[2:0] = 000 -> uo_out = 0000_0001
    ui_in[2:0] = 001 -> uo_out = 0000_0010
    ui_in[2:0] = 010 -> uo_out = 0000_0100
    ui_in[2:0] = 011 -> uo_out = 0000_1000
    ui_in[2:0] = 100 -> uo_out = 0001_0000
    ui_in[2:0] = 101 -> uo_out = 0010_0000
    ui_in[2:0] = 110 -> uo_out = 0100_0000
    ui_in[2:0] = 111 -> uo_out = 1000_0000
"""

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    """Verify that each selector value activates exactly one output bit."""

    dut._log.info("Start seven-segment mapping test")

    # Start the clock.
    # The current mapping design is combinational and does not require
    # the clock, but keeping it running makes the test compatible with
    # both RTL and gate-level simulation.
    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # Put all inputs into known initial states.
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0

    # Apply reset.
    # Reset is not used by the temporary mapping design, but driving it
    # explicitly avoids unknown values during gate-level simulation.
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 2)
    dut.rst_n.value = 1
    await ClockCycles(dut.clk, 1)

    # Test all eight selector values.
    for selector in range(8):
        # ui_in[2:0] carries the selector.
        # Bits ui_in[7:3] remain zero.
        dut.ui_in.value = selector

        # Wait for the output to settle.
        await ClockCycles(dut.clk, 1)

        # Exactly one output bit should be high.
        expected_output = 1 << selector
        actual_output = int(dut.uo_out.value)

        dut._log.info(
            f"selector={selector:03b}, "
            f"expected={expected_output:08b}, "
            f"actual={actual_output:08b}"
        )

        assert actual_output == expected_output, (
            f"Selector {selector:03b}: "
            f"expected uo_out={expected_output:08b}, "
            f"received uo_out={actual_output:08b}"
        )

        # The bidirectional pins are unused.
        assert int(dut.uio_out.value) == 0, (
            f"Expected uio_out=00000000, "
            f"received {int(dut.uio_out.value):08b}"
        )

        assert int(dut.uio_oe.value) == 0, (
            f"Expected uio_oe=00000000, "
            f"received {int(dut.uio_oe.value):08b}"
        )

    dut._log.info("All eight output mappings passed")
