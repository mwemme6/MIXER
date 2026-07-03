module main_prefix_adder (a, b, cin, sum, cout);
input  [3:0] a, b;
input        cin;
output [3:0] sum;
output       cout;

wire [3:0] p, g;
wire       c1, c2, c3, c4;

wire       G10, P10;
wire       G20, P20;
wire       G30, P30;

wire       G21, P21;
wire       G31, P31;

// bitwise propagate and generate
assign p[0] = a[0] ^ b[0];
assign p[1] = a[1] ^ b[1];
assign p[2] = a[2] ^ b[2];
assign p[3] = a[3] ^ b[3];

assign g[0] = a[0] & b[0];
assign g[1] = a[1] & b[1];
assign g[2] = a[2] & b[2];
assign g[3] = a[3] & b[3];

// prefix level 1
assign G10 = g[1] | (p[1] & g[0]);
assign P10 = p[1] & p[0];

assign G20 = g[2] | (p[2] & g[1]);
assign P20 = p[2] & p[1];

assign G30 = g[3] | (p[3] & g[2]);
assign P30 = p[3] & p[2];

// prefix level 2
assign G21 = G20 | (P20 & g[0]);
assign P21 = P20 & p[0];

assign G31 = G30 | (P30 & G10);
assign P31 = P30 & P10;

// carry computation
assign c1 = g[0] | (p[0] & cin);
assign c2 = G10  | (P10 & cin);
assign c3 = G21  | (P21 & cin);
assign c4 = G31  | (P31 & cin);

// sum bits
assign sum[0] = p[0] ^ cin;
assign sum[1] = p[1] ^ c1;
assign sum[2] = p[2] ^ c2;
assign sum[3] = p[3] ^ c3;

assign cout = c4;

endmodule