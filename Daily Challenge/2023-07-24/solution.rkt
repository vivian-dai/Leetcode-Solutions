(define/contract (my-pow x n)
  (-> flonum? exact-integer? flonum?)
    (cond
        [(equal? n 0) 1.0]
        [(negative? n) (/ 1.0 (my-pow x (* -1 n)))]
        [(equal? (remainder n 2) 0) (my-pow (* x x) (/ n 2))]
        [else (* x (my-pow (* x x) (/ (sub1 n) 2)))])
  )
