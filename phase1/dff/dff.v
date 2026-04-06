module dff (
    input clk,
    input rst,
    input d,
    output reg q
);

always @(posedge clk) begin
    if (rst)
        q <= 1'b0;
    else
        q <= d;
end

initial begin
    $dumpfile("dump.vcd");
    $dumpvars(0, dff);
end

endmodule