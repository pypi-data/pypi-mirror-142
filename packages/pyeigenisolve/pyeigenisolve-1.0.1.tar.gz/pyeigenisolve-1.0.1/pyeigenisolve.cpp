// #include <iostream>
#include <cfloat>
#include <vector>
#include <Eigen/SparseCore>
#include <Eigen/IterativeLinearSolvers>

// #define printit(x) std::cout << #x ":\n" << x << "\n\n"
#define printit(x) 
#define sign(x) ((x > 0) - (x < 0))
#define max(x, y) ( x > y ? x : y)
#define min(x, y) ( x > y ? y : x)

/* stable implementation from scipy
    https://github.com/scipy/scipy/blob/v1.7.1/scipy/sparse/linalg/isolve/lsqr.py#L96-L572
  that is from 
    S.-C. Choi, "Iterative Methods for Singular Linear Equations
        and Least-Squares Problems", Dissertation,
        http://www.stanford.edu/group/SOL/dissertations/sou-cheng-choi-thesis.pdf
*/
void sym_ortho(double a, double b, double& c, double& s, double& r) {
  if (b == 0) {
        c = sign(a);
        s = 0;
        r = abs(a);
    } else if (a == 0) {
        c = 0;
        s = sign(b);
        r = abs(b);
    } else if (abs(b) > abs(a)) {
        double tau = a / b;
        s = sign(b) / sqrt(1 + tau * tau);
        c = s * tau;
        r = b / s;
    } else {
        double tau = b / a;
        c = sign(a) / sqrt(1+tau*tau);
        s = c * tau;
        r = a / c;
    }
}

Eigen::VectorXd LSMR(
  const Eigen::SparseMatrix<double> &A, 
  const Eigen::VectorXd &b, 
  const Eigen::VectorXd &x_ini, 
  const double a_tol,
  const double b_tol,
  const double conlim,
  const double lambda,
  const int maxiters,
  int64_t* out_istop,
  int64_t* out_niters)
{
  *out_istop = 0;
  // double a_tol = 1e-6; double b_tol = 1e-6;
  // double lambda = 0; double conlim = 1e+8;
  
  // stopping crit
  double normb = b.norm();
  Eigen::VectorXd x = x_ini;

  Eigen::VectorXd u = b - A * x;
  double beta = u.norm();
  u.normalize();
  
  Eigen::VectorXd v = A.transpose()*u;
  double alpha = v.norm();
  v.normalize();
  
  int m = A.rows();
  int n = A.cols();
  
  // vars for first iter
  int iter = 0;
  double zetabar = alpha * beta;
  double alphabar = alpha;
  double rho = 1.0;
  double rhobar = 1.0;
  double cbar = 1.0;
  double sbar = 0.0;
  
  Eigen::VectorXd h = v;
  Eigen::VectorXd hbar = Eigen::VectorXd::Zero(n);
  
  // vars for estimating ||r||
  double betadd = beta;
  double betad = 0.0;
  double rhodold = 1.0;
  double tautildeold = 0.0;
  double thetatilde = 0.0;
  double zeta = 0.0;
  double d = 0.0;
  
  // init vars for estimating ||A|| and cond(A)
  double normA2 = alpha*alpha;
  double maxrbar = 0.0;
  double minrbar = 1e100;
  
  //double istop = 0;
  double ctol = 0;
  if (conlim > 0)
    ctol = 1.0/conlim;
  double normr = beta;
  
  double normAr = alpha*beta;
  if (normAr == 0) {
    // cout << "exact solution is 0" << endl;
    return x;
  }
  
  while (iter < maxiters) {  // loop count = 100
    u = A*v - alpha*u;
    beta = u.norm();
    if (beta > 0) {
      u.normalize();
      v = A.transpose()*u - beta*v;
      alpha = v.norm();
      if (alpha > 0) 
        v.normalize();
    }
    
    // construct rotation Qhat
    // double alphahat = sqrt(alphabar*alphabar + lambda*lambda);  // no regularization term
    // double chat = alphabar/alphahat;
    // double shat = lambda/alphahat;
    double chat, shat, alphahat;
    sym_ortho(alphabar, lambda, chat, shat, alphahat);
    
    // plane rotations...
    
    double rhoold = rho;

    // rho = sqrt(alphahat*alphahat + beta*beta);
    // double c = alphahat/rho;
    // double s = beta/rho;
    double c, s;
    sym_ortho(alphahat, beta, c, s, rho);

    double thetanew = s*alpha;
    alphabar = c*alpha;
        
    double rhobarold = rhobar;
    double zetaold = zeta;
    double thetabar = sbar*rho;
    double rhotemp = cbar*rho;

    // rhobar = sqrt( cbar*rho*cbar*rho + thetanew*thetanew );
    // cbar *= rho/rhobar;
    // sbar = thetanew/rhobar;
    sym_ortho(cbar * rho, thetanew, cbar, sbar, rhobar);
    
    zeta = cbar*zetabar;
    zetabar = -sbar*zetabar;
    
    // update h, h_hat, x
    //cout << thetabar << ", " << rho << ", " << rhoold << ", " << rhobarold << endl;
    hbar = h - (thetabar*rho/(rhoold*rhobarold))*hbar;
    //cout << hbar << endl;
    //cout << zeta << ", " << rho << ", " << rhobar << endl;
    x += (zeta/(rho*rhobar))*hbar;
    //cout << x << endl;
    h = v - (thetanew/rho)*h;
    
    // estimate of ||r||
    double betaacute = chat*betadd;
    double betacheck = -shat*betadd;
    
    double betahat = c*betaacute;
    betadd = -s*betaacute;
    
    double thetatildeold = thetatilde;
    double rhotildeold;// = sqrt( rhodold*rhodold + thetabar*thetabar );
    double ctildeold;// = rhodold/rhotildeold;
    double stildeold;// = thetabar/rhotildeold;
    sym_ortho(rhodold, thetabar, ctildeold, stildeold, rhotildeold);

    thetatilde = stildeold*rhobar;
    rhodold = ctildeold*rhobar;
    betad = -stildeold*betad + ctildeold*betahat;
    
    tautildeold = (zetaold - thetatildeold*tautildeold)/rhotildeold;
    double taud = (zeta - thetatilde*tautildeold)/rhodold;
    d = d + betacheck*betacheck;
    normr = sqrt(d + (betad - taud)*(betad - taud) + betadd*betadd);
    
    // estimate ||A||
    normA2 += beta*beta;
    double normA = sqrt(normA2);
    normA2 += alpha*alpha;
    
    maxrbar = max(maxrbar, rhobarold);
    if (iter > 1)
      minrbar = min(minrbar, rhobarold);
    double condA = max(maxrbar, rhotemp)/min(minrbar, rhotemp);
    
    // stopping crtierion
    normAr = abs(zetabar);
    double normx = x.norm();
    
    double test1 = normr/normb;
    double test2 = normAr / (normA*normr);
    double test3 = 1.0/condA;
    double t1 = test1 / (1 + normA*normx/normb);
    double rtol = b_tol + a_tol*normA*normx/normb;
    
    // skip error checking
    
    // check tests
    if (test3 <= ctol) {
      *out_istop = 3;
      break;
    } else if (test2 <= a_tol) {
      *out_istop = 2;
      break;
    } else if (test1 <= rtol) {
      *out_istop = 1;
      break;
    }
    
    //printf("%d\t%f\t%0.3f\t%0.3f\t%f\t%0.1f\n", iter, x(0), normr, normAr, test1,test2);
    
    iter++;
  }

  *out_niters = iter;
  if (*out_istop == 0) {
    *out_istop = 7;
  }
  
  //cout << x << endl;
  return x;
}

Eigen::VectorXd LSQR(
  const Eigen::SparseMatrix<double> &A, 
  const Eigen::VectorXd &b, 
  const Eigen::VectorXd &x_ini, 
  const double &eps, 
  int max_iters,
  int64_t* out_istop,
  int64_t* out_niters)
{
  *out_istop = 0;

	/******************************
	* Initialize
	******************************/
  Eigen::VectorXd x = x_ini;
  // printit(A);
  // printit(b);
  // printit(eps);
  // printit(max_iters);

	double beta = (b - A * x).norm();
	Eigen::VectorXd u = (b - A * x) / beta;
	Eigen::VectorXd ATu = A.transpose() * u;
	double alpha = ATu.norm();
	Eigen::VectorXd v = ATu/alpha;
	Eigen::VectorXd w = v;
	double phi_bar = beta;
	double rho_bar = alpha;
	
	/***
	* Variables for stopping criteria
	****/
	double z = 0;
	double cs2 = -1;
	double sn2 = 0;
	double ddnorm = 0;
	const double bnorm = beta;
	double rnorm = beta;
	double xnorm = 0;
	double xxnorm = 0;
	double Anorm = 0;
	double Acond = 0;

	int itr = 0;
	while (itr < max_iters) {
    // printit(itr);
    // std::cout << "x:\n" << x << "\n\n";
		
		/*************************************
		* Continue the bidiagnolization
		**************************************/
		Eigen::VectorXd rhs_beta = A * v - alpha * u;
		beta = rhs_beta.norm();
    // printit(beta);
		u = rhs_beta / beta;

		Eigen::VectorXd rhs_alpha = A.transpose() * u  - beta * v;
		alpha = rhs_alpha.norm();
    // printit(alpha);
		v = rhs_alpha / alpha;

		/*************************************
		* Constract and apply next orthogonal transformation
		**************************************/

		// double rho = sqrt(rho_bar * rho_bar + beta * beta);
		// double c = rho_bar / rho;
		// double s = beta / rho;

    double rho=0, c=0, s=0;
    sym_ortho(rho_bar, beta, c, s, rho);
    // std::cout << "#" << itr << ": ";
    // std::cout << "rho_bar=" << rho_bar << ", ";
    // std::cout << "beta=" << beta << ", ";
    // std::cout << "c=" << c << ", ";
    // std::cout << "s=" << s << ", ";
    // std::cout << "rho=" << rho << "\n";

    // printit(rho);
    // printit(c);
    // printit(s);

		double theta = s * alpha;
    // printit(theta);
		rho_bar = -c* alpha;
    // printit(rho_bar);
		double phi = c * phi_bar;
    // printit(phi);
		phi_bar = s*phi_bar;
    // printit(phi_bar);

		/*************************************
		* Test for convergence
		**************************************/

		double gambar = -cs2 *rho;
    // printit(gambar);
		double rhs = phi - sn2 * rho * z;
    // printit(rhs);
		double zbar = rhs / gambar;
    // printit(zbar);
		xnorm = sqrt(xxnorm + zbar * zbar);
    // printit(xnorm);
		double gamma = sqrt(gambar* gambar + theta* theta);
    // printit(gamma);
		cs2 = gambar / gamma;
    // printit(cs2);
		sn2 = theta / gamma;
    // printit(sn2);
		z = rhs / gamma;
    // printit(z);
		xxnorm += z * z;
    // printit(xxnorm);

		
		Eigen::VectorXd rhow = (1 / rho) * w;

		/*************************************
		* Update x, w
		**************************************/
		x = x + (phi / rho) * w;
    // printit(x);
		w = v - (theta / rho) * w;
    // printit(w);

		ddnorm = ddnorm + rhow.norm() * rhow.norm();
    // printit(ddnorm);
		Anorm = sqrt(Anorm * Anorm + alpha * alpha + beta * beta);
    // printit(Anorm);
		Acond = Anorm + sqrt(ddnorm);
    // printit(Acond);
		rnorm = phi_bar;
    // printit(rnorm);
		double Arnorm = alpha * abs(s * phi);
    // printit(Arnorm);
		double test1 = rnorm / bnorm;
		double test2 = 0;
		double test3 = 0;
		if (Anorm == 0 || rnorm == 0){
			test2 = DBL_MAX;
		}
		else{
			test2 = Arnorm / (Anorm * rnorm);
		}
    // printit(test2);
		if (Acond == 0){
			test3 = DBL_MAX;
		}
		else{
			test3 = 1 / Acond;
		}
    // printit(test3);
		double t1 = test1 / (1 + Anorm*xnorm / bnorm);
    // printit(t1);
		double rtol = eps + eps * Anorm * xnorm / bnorm;
    // printit(rtol);
		
		itr++;
    if (test3 <= eps) {
      *out_istop = 3;
      break;
    } else if (test2 <= eps) {
      *out_istop = 2;
      break;
    } else if (test1 <= rtol) {
      *out_istop = 1;
      break;
    }

	}

  *out_niters = itr;
  if (*out_istop == 0) {
    *out_istop = 7;
  }

  return x;
}

extern "C" {
void lscg(
  int64_t rows,
  int64_t cols,
  int64_t nentries,
  const int32_t* i,
  const int32_t* j,
  const double* entries,
  double* y,
  double* x0,
  double* out,
  double tol,
  int64_t maxiters,
  int64_t* out_istop,
  int64_t* out_niters
) {
  // std::cout << "i: " << i[0] << ", " << i[1] << std::endl;

  typedef Eigen::Triplet<double> T;
  std::vector<T> tripletList;
  tripletList.reserve(nentries);
  for (int index=0; index < nentries; index++)
  {
    // std::cout << "#" << index << ": " << i[index] << ", " << j[index] << ": " << entries[index] << std::endl;
    tripletList.push_back(T(i[index],j[index],entries[index]));
  }

  Eigen::SparseMatrix<double> A(rows,cols);
  A.setFromTriplets(tripletList.begin(), tripletList.end());

  Eigen::LeastSquaresConjugateGradient<Eigen::SparseMatrix<double> > lscg;
  lscg.setTolerance(tol);
  lscg.setMaxIterations(maxiters);
  lscg.compute(A);

  Eigen::Map<Eigen::VectorXd> y_(y, rows);
  Eigen::VectorXd x(rows);
  Eigen::VectorXd x0_ = Eigen::VectorXd::Map(x0, cols);

  x = lscg.solveWithGuess(y_, x0_);
  // std::cout << "x: " << x << std::endl;
  memcpy(out, x.data(), sizeof(double) * cols);

  Eigen::ComputationInfo info = lscg.info();
  *out_niters = lscg.iterations();
  if (info == Eigen::Success) {
    *out_istop = 1;
  } else {
    *out_istop = 7;
  }
}

////////////////////////////////////////////////////////

void lsqr(
  int64_t rows,
  int64_t cols,
  int64_t nentries,
  const int32_t* i,
  const int32_t* j,
  const double* entries,
  double* y,
  double* x0,
  double* out,
  double eps,
  int64_t maxiters,
  int64_t* out_istop,
  int64_t* out_niters
) {
  // std::cout << "i: " << i[0] << ", " << i[1] << std::endl;

  typedef Eigen::Triplet<double> T;
  std::vector<T> tripletList;
  tripletList.reserve(nentries);
  for (int index=0; index < nentries; index++)
  {
    // std::cout << "#" << index << ": " << i[index] << ", " << j[index] << ": " << entries[index] << std::endl;
    tripletList.push_back(T(i[index],j[index],entries[index]));
  }

  Eigen::SparseMatrix<double> A(rows,cols);
  A.setFromTriplets(tripletList.begin(), tripletList.end());

  Eigen::Map<Eigen::VectorXd> b(y, rows);
  Eigen::VectorXd x = LSQR(A, b, Eigen::VectorXd::Map(x0, cols), eps, maxiters, out_istop, out_niters);

  // std::cout << "x: " << x << std::endl;
  memcpy(out, x.data(), sizeof(double) * cols);
}

////////////////////////////////////////////////////////

void lsmr(
  int64_t rows,
  int64_t cols,
  int64_t nentries,
  const int32_t* i,
  const int32_t* j,
  const double* entries,
  double* y,
  double* x0,
  double* out,
  double a_tol,
  double b_tol,
  double conlim,
  double lambda,
  int64_t maxiters,
  int64_t* out_istop,
  int64_t* out_niters
) {
  // std::cout << "i: " << i[0] << ", " << i[1] << std::endl;

  typedef Eigen::Triplet<double> T;
  std::vector<T> tripletList;
  tripletList.reserve(nentries);
  for (int index=0; index < nentries; index++)
  {
    // std::cout << "#" << index << ": " << i[index] << ", " << j[index] << ": " << entries[index] << std::endl;
    tripletList.push_back(T(i[index],j[index],entries[index]));
  }

  Eigen::SparseMatrix<double> A(rows,cols);
  A.setFromTriplets(tripletList.begin(), tripletList.end());

  Eigen::Map<Eigen::VectorXd> b(y, rows);
  Eigen::VectorXd x = LSMR(
    A,
    b,
    Eigen::VectorXd::Map(x0, cols),
    a_tol,
    b_tol,
    conlim,
    lambda,
    maxiters,
    out_istop,
    out_niters
  );

  // std::cout << "x: " << x << std::endl;
  memcpy(out, x.data(), sizeof(double) * cols);
}
}

int main()
{
  int32_t i[] = {0, 1, 2, 2};
  int32_t j[] = {0, 1, 0, 1};
  double entries[] = {1, 1, 1, 1};
  double y[] = {2, 3, 5};
  double x0[] = {0, 0};
  double out[] = {0, 0};
  int64_t istop;
  int64_t niters;

  lscg(3, 2, 4, i, j, entries, y, x0, out, 1e-6, 1000, &istop, &niters);

  // for (int index=0; index < 2; index++) {
  //   std::cout << out[index] << " ";
  // }
  // std::cout << std::endl;

  return (out[0] == 2. & out[1] == 3.);
}
