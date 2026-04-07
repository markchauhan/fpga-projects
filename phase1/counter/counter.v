module counter (
    input clk, 
    input rst, 
    input ena, 
    output reg [3:0] q
);

always @(posedge clk) begin
  if (rst)
    q <= 4'b0000;
  else if (ena)
    q <= q + 1;
end

endmodule