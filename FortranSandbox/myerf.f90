PROGRAM error_function

	IMPLICIT NONE

	real(kind=8) :: x=0.d0, y=0.d0, h=1.d0
	real(kind=8), parameter ::  pi=acos(-1.d0)
	integer :: fct=1,k=0,n=1000
	logical :: sgnflag=.false.

	print *, "erf(x) at x = ?"
	read *, x

	if (x<0) then
	    sgnflag = .true.
	    x=abs(x)
	endif
 
	if (x<=1) then
	    do k=0,10
	        if (k==0) then
	            fct = 1
	        else if (k==1) then
		    fct = 1
	        else
		    fct = fct*k
	        endif
		y = y + (-1)**k*x**(2*k+1)/((2*k+1)*fct)
	    enddo
	    y = y*2/sqrt(pi)
	else if (x>1.and.x<3.47) then
	    y = 0.d0
	    h = (x-1)/n
	    do k=1,n-1
		y = y + exp(-(1+k*h)**2)
	    enddo
	    y = 0.84270079 + h*(exp(-1.d0)*0.5 + exp(-x**2)*0.5 + y)*2/sqrt(pi)
	else if (x>=3.47) then
	    y = 1
	endif

	if (sgnflag) then
	    y = -y
	    x = -x
	endif
	print *, "         x                   erf(x)"
	print "(f20.6, f20.6)", x,y
END PROGRAM error_function
