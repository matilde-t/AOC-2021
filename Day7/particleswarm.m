function [x, fval, exitflag, output] = particleswarm (varargin)
  ## parse and validate input 
  p = inputParser ();
  p.FunctionName = "particleswarm";
  p.addRequired ("fun");
  p.addRequired ("nvars");
  p.addOptional ("lb", []);
  p.addOptional ("ub", []);
  val_Display = @(x) any (strcmp (tolower (x), {"off", "final", "iter"}));
  p.addParameter ("Display", "final", val_Display);
  val_int = @(x) isscalar (x) && isnumeric (x) && x > 0;
  p.addParameter ("DisplayInterval", 1, val_int);
  val_float = @(x) isscalar (x) && isnumeric (x);
  p.addParameter ("FunctionTolerance", 1e-6, val_float);
  val_InertiaRange = @(x) isvector (x) && (all (x >= 0) || all (x <= 0));
  p.addParameter ("InertiaRange", NaN, val_InertiaRange);
  p.addParameter ("MaxIterations", NaN, val_int);
  p.addParameter ("MaxStallIterations", 20, val_int);
  p.addParameter ("MaxStallTime", Inf, val_float);
  p.addParameter ("MaxTime", Inf, val_float);
  p.addParameter ("ObjectiveLimit", -Inf, val_float);
  p.addParameter ("SelfAdjustmentWeight", NaN, val_float);
  p.addParameter ("SocialAdjustmentWeight", NaN, val_float);
  p.addParameter ("SwarmSize", NaN, val_int);
  
  p.parse (varargin{:});
  fun = p.Results.fun;
  nvars = p.Results.nvars;
  lb = p.Results.lb;
  ub = p.Results.ub;
  Display = p.Results.Display;
  DisplayInterval = p.Results.DisplayInterval;
  FunctionTolerance = p.Results.FunctionTolerance;
  InertiaRange = p.Results.InertiaRange;
  MaxIterations = p.Results.MaxIterations;
  MaxStallIterations = p.Results.MaxStallIterations;
  MaxStallTime = p.Results.MaxStallTime;
  MaxTime = p.Results.MaxTime;
  ObjectiveLimit = p.Results.ObjectiveLimit;
  SelfAdjustmentWeight = p.Results.SelfAdjustmentWeight;
  SocialAdjustmentWeight = p.Results.SocialAdjustmentWeight;
  SwarmSize = p.Results.SwarmSize;
  
  if typeinfo (fun) != "function handle"
    error ("first argument must be fun handle");
  endif
  validateattributes (nvars, {"numeric", "scalar", "nonnan", "nonnegative",...
  "nonzero"}, {});
  if sum (find (lb > ub)) > 0
    exitflag = -2;
    error ("inconsistent bounds")
  endif
  if max (size (lb)) == 0
    lb = -1000*ones(1,nvars);
  endif
  if max (size (ub)) == 0
    ub = 1000*ones(1,nvars);
  endif
  validateattributes (lb, {"numeric", "nonnan", "vector"}, {"numel", nvars});
  validateattributes (ub, {"numeric", "nonnan", "vector"}, {"numel", nvars});
  if ! isnan(InertiaRange)
    validateattributes (InertiaRange, {"nondecreasing"}, {"numel", 2});
    if any (InertiaRange >= 0)
      Inertia = max (InertiaRange);
    else
      Inertia = min (InertiaRange);
    endif
  else
    Inertia = InertiaRange;
  endif
  if isnan (MaxIterations)
    MaxIterations = 200*nvars;
  endif
  
##  [SwarmSize, Inertia, SocialAdjustmentWeight, SelfAdjustmentWeight] ...
##  = PSOcheckCase (nvars, MaxIterations, SwarmSize, Inertia, ...
##  SocialAdjustmentWeight, SelfAdjustmentWeight);
  
  ## validate output
  nargoutchk (0, 4)
  
  ######
  # TODO: if there is an unbounded component, particleswarm creates
  # particles with a random uniform distribution from –1000 to 1000.
  # If you have only one bound, particleswarm shifts the creation
  # to have the bound as an endpoint, and a creation interval 2000 wide.
  # Particle i has position x(i), which is a row vector with nvars
  # elements. Control the span of the initial swarm using the 
  # InitialSwarmSpan option.
  ######
  diff = abs (ub-lb);
  x = diff.*rand (SwarmSize, nvars) + lb; # N. B. the position is a row 
  # vector with nvars elements
  p = x;
  ######
  # TODO: Similarly, particleswarm creates initial particle velocities v at
  # random uniformly within the range [-r,r], where r is the vector of initial
  # ranges. The range of component k is min(ub(k) - lb(k),InitialSwarmSpan(k)).
  ######
  v = 2*diff.*rand (SwarmSize, nvars) - diff;
  for i = 1:SwarmSize
    f(i) = fun(x(i,:));
  endfor
  [b idx] = min (f);
  d = x(idx,:);
  
  flag = false;
  Inertia = max (InertiaRange);
  Iteration = 0;
  StallIterations = 0;
  Tolerance = Inf;
  StallTime = 0;
  Time = 0;
  diffMatrix = repmat(diff, SwarmSize, 1);
  lbMatrix = repmat(lb, SwarmSize, 1);
  ubMatrix = repmat(ub, SwarmSize, 1);
  

  Inertia = 0.3925;
  SelfAdjustmentWeight = 2.5586;
  SocialAdjustmentWeight = 1.3358;
  
  
  do
    Iteration = Iteration + 1;
    
    ## update velocity
    u1 = rand (1, nvars);
    u2 = rand (1, nvars);
    v = Inertia*v + SelfAdjustmentWeight*u1.*(p-x) + SocialAdjustmentWeight...
    *u2.*(d-x);
    
    ## bound velocity
    BoundIdx = find (v < -diffMatrix);
    if sum (BoundIdx) > 0
      v(BoundIdx) = -diffMatrix(BoundIdx);
    endif
    BoundIdx = find (v > diffMatrix);
    if sum (BoundIdx) > 0
      v(BoundIdx) = diffMatrix(BoundIdx);
    endif
    
    ## update position
    x = x + v;
    
    ## bound position
    BoundIdx = find (x < lbMatrix);
    if sum (BoundIdx) > 0
      x(BoundIdx) = lbMatrix(BoundIdx);
    endif
    BoundIdx = find (x > ubMatrix);
    if sum (BoundIdx) > 0
      x(BoundIdx) = ubMatrix(BoundIdx);
    endif
    
    ## update particle's best and global best
    for i = 1:SwarmSize
      if fun (x(i,:)) < fun (p(i,:))
        p(i,:) = x(i,:);
      endif
      if fun (x(i,:)) < b
        Tolerance = abs (fun (x(i,:)) - b);
        b = fun (x(i,:));
        d = x(i,:);
      endif
    endfor
    
    ## check stopping criteria
    if Tolerance < FunctionTolerance
      exitflag = 1;
      flag = true;
    elseif StallIterations > MaxStallIterations
      exitflag = 1;
      flag = true;
    elseif Iteration > MaxIterations
      exitflag = 0;
      flag = true;
    elseif f < ObjectiveLimit
      exitflag = -3;
      flag = true;
    elseif StallTime > MaxStallTime
      exitflag = -4;
      flag = true;
    elseif Time > MaxTime
      exitflag = -5;
      flag = true;
    else
      flag = false;
    endif
  until flag
  x = d;
  fval = fun(x);
  endfunction