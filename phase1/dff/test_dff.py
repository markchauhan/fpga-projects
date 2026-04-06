import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge

@cocotb.test()
async def test_dff(dut):
    cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())

    dut.rst.value = 1
    dut.d.value = 0
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)
    assert dut.q.value == 0

    dut.rst.value = 0
    dut.d.value = 1
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)
    assert dut.q.value == 1

    dut.d.value = 0
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)
    assert dut.q.value == 0