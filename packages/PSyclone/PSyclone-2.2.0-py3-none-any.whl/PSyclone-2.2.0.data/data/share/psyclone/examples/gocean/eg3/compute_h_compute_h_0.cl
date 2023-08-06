__attribute__((reqd_work_group_size(4, 1, 1)))
__kernel void compute_h_code(
  __global double * restrict h,
  __global double * restrict p,
  __global double * restrict u,
  __global double * restrict v,
  int xstart,
  int xstop,
  int ystart,
  int ystop
  ){
  int hLEN1 = get_global_size(0);
  int hLEN2 = get_global_size(1);
  int pLEN1 = get_global_size(0);
  int pLEN2 = get_global_size(1);
  int uLEN1 = get_global_size(0);
  int uLEN2 = get_global_size(1);
  int vLEN1 = get_global_size(0);
  int vLEN2 = get_global_size(1);
  int i = get_global_id(0);
  int j = get_global_id(1);
  if ((!(((i < xstart) || (i > xstop)) || ((j < ystart) || (j > ystop))))) {
    h[i + j * hLEN1] = (p[i + j * pLEN1] + (0.25e0 * ((((u[(i + 1) + j * uLEN1] * u[(i + 1) + j * uLEN1]) + (u[i + j * uLEN1] * u[i + j * uLEN1])) + (v[i + (j + 1) * vLEN1] * v[i + (j + 1) * vLEN1])) + (v[i + j * vLEN1] * v[i + j * vLEN1]))));
  }
}

