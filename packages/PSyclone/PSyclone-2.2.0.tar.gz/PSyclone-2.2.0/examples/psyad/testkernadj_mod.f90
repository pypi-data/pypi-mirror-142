module testkern_mod_adj
  implicit none
  public

  public :: testkern_code_adj

  contains
  subroutine testkern_code_adj(ascalar, field1, field2, npts)
    real, intent(in) :: ascalar
    integer, intent(in) :: npts
    real, dimension(npts), intent(inout) :: field2
    real, dimension(npts), intent(inout) :: field1
    real :: tmp
    real :: tmp2

    tmp = ascalar * ascalar
    tmp2 = tmp * 3.0
    field1(1) = field1(1) + field2(1) / tmp2
    field2(1) = field2(1) + field1(1)
    field1(1) = tmp * field1(1)

  end subroutine testkern_code_adj

end module testkern_mod_adj
