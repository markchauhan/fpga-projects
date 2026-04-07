import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_counter(dut):
    cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())

    # Apply reset
    dut.rst.value = 1
    dut.ena.value = 0
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)
    await FallingEdge(dut.clk)  # sample after RTL settles
    assert dut.q.value == 0, "Q should be 0 after reset"

    # Release reset, enable counting
    dut.rst.value = 0
    dut.ena.value = 1

    # Count up to 15 and check each value
    for i in range(1, 16):
        await RisingEdge(dut.clk)   # trigger count
        await FallingEdge(dut.clk)  # sample after RTL settles
        assert dut.q.value == i, f"Expected {i}, got {dut.q.value}"

    # Check rollover — next count should wrap to 0
    await RisingEdge(dut.clk)
    await FallingEdge(dut.clk)
    assert dut.q.value == 0, "Counter should wrap to 0 after 15"

    # Test enable — hold value when ena low
    dut.ena.value = 0
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)
    await FallingEdge(dut.clk)
    assert dut.q.value == 0, "Counter should hold when enable is low"
