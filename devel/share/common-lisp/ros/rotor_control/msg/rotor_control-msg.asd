
(cl:in-package :asdf)

(defsystem "rotor_control-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :actionlib_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "qrotorMoveAction" :depends-on ("_package_qrotorMoveAction"))
    (:file "_package_qrotorMoveAction" :depends-on ("_package"))
    (:file "qrotorMoveActionFeedback" :depends-on ("_package_qrotorMoveActionFeedback"))
    (:file "_package_qrotorMoveActionFeedback" :depends-on ("_package"))
    (:file "qrotorMoveActionGoal" :depends-on ("_package_qrotorMoveActionGoal"))
    (:file "_package_qrotorMoveActionGoal" :depends-on ("_package"))
    (:file "qrotorMoveActionResult" :depends-on ("_package_qrotorMoveActionResult"))
    (:file "_package_qrotorMoveActionResult" :depends-on ("_package"))
    (:file "qrotorMoveFeedback" :depends-on ("_package_qrotorMoveFeedback"))
    (:file "_package_qrotorMoveFeedback" :depends-on ("_package"))
    (:file "qrotorMoveGoal" :depends-on ("_package_qrotorMoveGoal"))
    (:file "_package_qrotorMoveGoal" :depends-on ("_package"))
    (:file "qrotorMoveResult" :depends-on ("_package_qrotorMoveResult"))
    (:file "_package_qrotorMoveResult" :depends-on ("_package"))
  ))