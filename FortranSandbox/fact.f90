PROGRAM factorial

	IMPLICIT NONE

	integer :: k, f=1, n

	print *, "Determine factorial of k = ?"
	read *, n
	
	if (n==0) then
	    f=1
	else if (n==1) then
	    f=1 
	else
	    do k=2,n
	        f=f*k
		enddo
	    endif
	print *, "n! = ", f
END PROGRAM factorial
