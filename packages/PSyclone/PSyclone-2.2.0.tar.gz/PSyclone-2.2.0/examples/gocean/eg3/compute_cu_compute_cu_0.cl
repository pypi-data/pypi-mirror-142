__attribute__((reqd_work_group_size(4, 1, 1)))
__kernel void compute_cu_code(
  __global double * restrict cu,
  __global double * restrict p,
  __global double * restrict u,
  int xstart,
  int xstop,
  int ystart,
  int ystop
  ){
  int cuLEN1 = get_global_size(0);
  int cuLEN2 = get_global_size(1);
  int pLEN1 = get_global_size(0);
  int pLEN2 = get_global_size(1);
  int uLEN1 = get_global_size(0);
  int uLEN2 = get_global_size(1);
  int i = get_global_id(0);
  int j = get_global_id(1);
  if ((!(((i < xstart) || (i > xstop)) || ((j < ystart) || (j > ystop))))) {
    cu[i + j * cuLEN1] = ((0.5e0 * (p[i + j * pLEN1] + p[(i - 1) + j * pLEN1])) * u[i + j * uLEN1]);
  }
}

