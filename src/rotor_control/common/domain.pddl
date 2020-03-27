(define (domain small-quadrotor-world)
   (:requirements :strips :typing)
   (:types quadrotor location height person)
   (:predicates 
      (checked ?x - location)  ;location
      (unChecked ?x - location)
      (pictured ?p - person)
      (unPictured ?p - person)
      (locationAdjust ?l1 - location ?l2 - location)
      (at_d ?d - quadrotor ?l - location)
      (at_p ?p - person ?l - location)
      (containObst ?l1 - location)
      (notContainObst ?l1 - location)
      (heightHigh ?d - quadrotor)
      (notHeightHigh ?d - quadrotor)
   )

   (:action moveBetweenSquares
      :parameters ( ?d - quadrotor ?l1 - location ?l2 - location)
      :precondition (and (at_d ?d ?l1) (locationAdjust ?l1 ?l2) (unChecked ?l2) (notContainObst ?l2) (heightHigh ?d))
      :effect (and (at_d ?d ?l2) (not (at_d ?d ?l1)) (checked ?l1) (checked ?l2) (not (unChecked ?l2)) )
   )
   (:action takepic
   :parameters ( ?d - quadrotor ?l1 - location ?p - person)
   :precondition (and (at_d ?d ?l1) (at_p ?p ?l1)  (unPictured ?p))
   :effect (and (pictured ?p) (not (unPictured ?p)))

   )

)
