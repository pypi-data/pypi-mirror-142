__attribute__((reqd_work_group_size(4, 1, 1)))
__kernel void compute_cv_code(
  __global double * restrict cv,
  __global double * restrict p,
  __global double * restrict v,
  int xstart,
  int xstop,
  int ystart,
  int ystop
  ){
  int cvLEN1 = get_global_size(0);
  int cvLEN2 = get_global_size(1);
  int pLEN1 = get_global_size(0);
  int pLEN2 = get_global_size(1);
  int vLEN1 = get_global_size(0);
  int vLEN2 = get_global_size(1);
  int i = get_global_id(0);
  int j = get_global_id(1);
  if ((!(((i < xstart) || (i > xstop)) || ((j < ystart) || (j > ystop))))) {
    cv[i + j * cvLEN1] = ((0.5e0 * (p[i + j * pLEN1] + p[i + (j - 1) * pLEN1])) * v[i + j * vLEN1]);
  }
}

