__attribute__((reqd_work_group_size(4, 1, 1)))
__kernel void compute_z_code(
  __global double * restrict z,
  __global double * restrict p,
  __global double * restrict u,
  __global double * restrict v,
  double dx,
  double dy,
  int xstart,
  int xstop,
  int ystart,
  int ystop
  ){
  int zLEN1 = get_global_size(0);
  int zLEN2 = get_global_size(1);
  int pLEN1 = get_global_size(0);
  int pLEN2 = get_global_size(1);
  int uLEN1 = get_global_size(0);
  int uLEN2 = get_global_size(1);
  int vLEN1 = get_global_size(0);
  int vLEN2 = get_global_size(1);
  int i = get_global_id(0);
  int j = get_global_id(1);
  if ((!(((i < xstart) || (i > xstop)) || ((j < ystart) || (j > ystop))))) {
    z[i + j * zLEN1] = ((((4.0e0 / dx) * (v[i + j * vLEN1] - v[(i - 1) + j * vLEN1])) - ((4.0e0 / dy) * (u[i + j * uLEN1] - u[i + (j - 1) * uLEN1]))) / (((p[(i - 1) + (j - 1) * pLEN1] + p[i + (j - 1) * pLEN1]) + p[i + j * pLEN1]) + p[(i - 1) + j * pLEN1]));
  }
}

