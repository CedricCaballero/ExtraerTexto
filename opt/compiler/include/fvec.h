//  Copyright (c) 2020 Intel Corporation.
//
//  SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception.

/*
 *  Definition of a C++ class interface to Intel(R) Streaming SIMD Extensions intrinsics.
 *
 *
 *	File name : fvec.h  Fvec class definitions
 *
 *	Concept: A C++ abstraction of Intel(R) Streaming SIMD Extensions designed to improve
 *
 *  programmer productivity. Speed and accuracy are sacrificed for utility.
 *
 *	Facilitates an easy transition to compiler intrinsics
 *
 *	or assembly language.
 *
 *	F32vec4:	4 packed single precision
 *				32-bit floating point numbers
*/

#ifndef FVEC_H_INCLUDED
#define FVEC_H_INCLUDED

#if !defined __cplusplus
	#error ERROR: This file is only supported in C++ compilations!
#endif /* !__cplusplus */

#include <ia32intrin.h>
#include <assert.h>
#include <ivec.h>

#pragma pack(push,16) /* Must ensure class & union 16-B aligned */

/* If using MSVC5.0, explicit keyword should be used */
#if (_MSC_VER >= 1100) || defined(__linux__) || defined(__unix__) || defined(__APPLE__)
        #define EXPLICIT explicit
#else
   #if (__INTEL_COMPILER)
        #define EXPLICIT explicit /* If MSVC4.x & Intel, use __explicit */
   #else
        #define EXPLICIT /* nothing */
        #pragma message( "explicit keyword not recognized")
   #endif
#endif

/* Figure out whether and how to define the output operators */
#if defined(_IOSTREAM_) || defined(_CPP_IOSTREAM) || defined(_GLIBCXX_IOSTREAM) || defined (_LIBCPP_IOSTREAM)
#define FVEC_DEFINE_OUTPUT_OPERATORS
#define FVEC_STD std::
#elif defined(_INC_IOSTREAM) || defined(_IOSTREAM_H_)
#define FVEC_DEFINE_OUTPUT_OPERATORS
#define FVEC_STD
#endif

/* Whether C++11 defaulted/deleted functions feature can be used.*/
#if (__cplusplus >= 201103L) && !defined(_DISALLOW_VEC_CPP11_DEFAULTED_FUNCTIONS)
/*
 * This specifically changes default and value initialization behavior:
 * void foo() {
 *      I8vec8 var1;            // default initialization
 *      const I8vec8 var2;      // const object default initialization
 *      I8vec8 var3 = I8vec8(); // value initialization
 *      ...
 * }
 * With use of C++11 defaulted functions the vec classes explicitly declare
 * to use compiler provided default ctor that performs no action (i.e. trivial).
 * As a consequence of that the value of variable "var1" in example above is
 * indeterminate. Otherwise (prior to C++11 or when disabled use of the feature)
 * user-provided default ctor is called (which explicitly performs
 * initialization to zero value). Another consequence of that is constant
 * object declaration ("var2") becomes ill-formed without user-provided
 * default ctor.
 *
 * That change may have noticeable performance impact when array of objects
 * is declared.
 * Although value initialization flow changes too (an object is first
 * zero initialized prior to default ctor) the final result
 * practically end up the same.
 */
#define FVEC_USE_CPP11_DEFAULTED_FUNCTIONS
#endif

const union
{
    int i[4];
    __m128 m;
} __f32vec4_abs_mask_cheat = {0x7fffffff, 0x7fffffff, 0x7fffffff, 0x7fffffff};

#define _f32vec4_abs_mask ((F32vec4)__f32vec4_abs_mask_cheat.m)

class F32vec4
{
protected:
    __m128 vec;
public:

	/* Constructors: __m128, 4 floats, 1 float/double */

#ifdef FVEC_USE_CPP11_DEFAULTED_FUNCTIONS
    F32vec4() = default;
#else
	F32vec4() { vec = _mm_setzero_ps(); }
#endif

	/* initialize 4 SP FP with __m128 data type */
	F32vec4(__m128 m)			{ vec = m;}

	/* initialize 4 SP FPs with 4 floats */
	F32vec4(float f3, float f2, float f1, float f0)	{ vec= _mm_set_ps(f3,f2,f1,f0); }

	/* Explicitly initialize each of 4 SP FPs with same float */
	EXPLICIT F32vec4(float f)	{ vec = _mm_set_ps1(f); }

	/* Explicitly initialize each of 4 SP FPs with same double */
	EXPLICIT F32vec4(double d)	{ vec = _mm_set_ps1((float) d); }

	/* Assignment operations */
	F32vec4 &operator =(const F32vec4 &a) { vec = a.vec; return *this; }

	F32vec4& operator =(float f) { vec = _mm_set_ps1(f); return *this; }

	F32vec4& operator =(double d) {
        vec = _mm_set_ps1((float) d);
        return *this;
    }

	/* Conversion functions */
	operator  __m128() const	{ return vec; }		/* Convert to __m128 */

 	/* Logical Operators */
	friend F32vec4 operator &(const F32vec4 &a, const F32vec4 &b) { return _mm_and_ps(a,b); }
	friend F32vec4 operator |(const F32vec4 &a, const F32vec4 &b) { return _mm_or_ps(a,b); }
	friend F32vec4 operator ^(const F32vec4 &a, const F32vec4 &b) { return _mm_xor_ps(a,b); }

	/* Arithmetic Operators */
	friend F32vec4 operator +(const F32vec4 &a, const F32vec4 &b) { return _mm_add_ps(a,b); }
	friend F32vec4 operator -(const F32vec4 &a, const F32vec4 &b) { return _mm_sub_ps(a,b); }
	friend F32vec4 operator *(const F32vec4 &a, const F32vec4 &b) { return _mm_mul_ps(a,b); }
	friend F32vec4 operator /(const F32vec4 &a, const F32vec4 &b) { return _mm_div_ps(a,b); }

	F32vec4& operator +=(const F32vec4 &a)
                        { return *this = _mm_add_ps(vec,a); }
	F32vec4& operator -=(const F32vec4 &a)
                        { return *this = _mm_sub_ps(vec,a); }
	F32vec4& operator *=(const F32vec4 &a)
                        { return *this = _mm_mul_ps(vec,a); }
	F32vec4& operator /=(const F32vec4 &a)
                        { return *this = _mm_div_ps(vec,a); }
	F32vec4& operator &=(const F32vec4 &a)
                        { return *this = _mm_and_ps(vec,a); }
	F32vec4& operator |=(const F32vec4 &a)
                        { return *this = _mm_or_ps(vec,a); }
	F32vec4& operator ^=(const F32vec4 &a)
                        { return *this = _mm_xor_ps(vec,a); }

	F32vec4& flip_sign () { return *this = _mm_xor_ps (_mm_set_ps1(-0.0), *this); }
	F32vec4 operator - () const { return  _mm_xor_ps (_mm_set_ps1(-0.0), *this); }
	void set_zero() { vec = _mm_setzero_ps(); }
	void init (float f0, float f1, float f2, float f3) { vec = _mm_set_ps(f3,f2,f1,f0); }
	/* Mixed vector-scalar operations */
	F32vec4& operator +=(const float &f) { return *this = _mm_add_ps(vec,_mm_set_ps1(f)); }
	F32vec4& operator -=(const float &f) { return *this = _mm_sub_ps(vec,_mm_set_ps1(f)); }
	F32vec4& operator *=(const float &f) { return *this = _mm_mul_ps(vec,_mm_set_ps1(f)); }
	F32vec4& operator /=(const float &f) { return *this = _mm_div_ps(vec,_mm_set_ps1(f)); }

	friend F32vec4 operator +(const F32vec4 &a, const float &f) { return _mm_add_ps(a, _mm_set_ps1(f)); }
	friend F32vec4 operator -(const F32vec4 &a, const float &f) { return _mm_sub_ps(a, _mm_set_ps1(f)); }
	friend F32vec4 operator *(const F32vec4 &a, const float &f) { return _mm_mul_ps(a, _mm_set_ps1(f)); }
	friend F32vec4 operator /(const F32vec4 &a, const float &f) { return _mm_div_ps(a, _mm_set_ps1(f)); }

	bool is_zero() const {
		__m128 a = _mm_setzero_ps();
		a = _mm_cmpeq_ps(a, *this);
		int k = _mm_movemask_ps(a);
		return (k == 0xF);
	}
	/* Dot product */
	void dot (float& p, const F32vec4& rhs) const {
		p = add_horizontal(*this * rhs);
	}
	float dot (const F32vec4& rhs) const {
		return (add_horizontal(*this * rhs));
	}
	/* Length */
	float length_sqr()  const { return dot(*this); }
	float length()  const {
		float f = dot(*this);
		__m128 f2 = _mm_set_ss(f);
		__m128 f3 = _mm_sqrt_ss(f2);
		return _mm_cvtss_f32(f3);
	}
	/* Normalize */
	bool normalize() { float l = length(); *this /= l; return true; }

	/* Horizontal Add */
	friend float add_horizontal(const F32vec4 &a)
	{
		F32vec4 ftemp = _mm_add_ps(a, _mm_movehl_ps(a, a));
		ftemp = _mm_add_ss(ftemp, _mm_shuffle_ps(ftemp, ftemp, 1));
		return _mm_cvtss_f32(ftemp);
	}
	/* Horizontal Mul */
	friend float mul_horizontal(const F32vec4 &a)
	{
		F32vec4 ftemp = _mm_mul_ps(a, _mm_movehl_ps(a, a));
		ftemp = _mm_mul_ss(ftemp, _mm_shuffle_ps(ftemp, ftemp, 1));
		return _mm_cvtss_f32(ftemp);
	}

	/* Square Root */
	friend F32vec4 sqrt(const F32vec4 &a)		{ return _mm_sqrt_ps(a); }
	/* Reciprocal */
	friend F32vec4 rcp(const F32vec4 &a)		{ return _mm_rcp_ps(a); }
	/* Reciprocal Square Root */
	friend F32vec4 rsqrt(const F32vec4 &a)		{ return _mm_rsqrt_ps(a); }
	/* Ceil */
	friend F32vec4 ceil(const F32vec4 &a)	{ return _mm_svml_ceil_ps(a); }
	/* Floor */
	friend F32vec4 floor(const F32vec4 &a)	{ return _mm_svml_floor_ps(a); }
	/* Round */
	friend F32vec4 round(const F32vec4 &a)	{ return _mm_svml_round_ps(a); }
	/* SVML functions */
	friend F32vec4 acos(const F32vec4 &a)    { return _mm_acos_ps(a);    }
	friend F32vec4 acosh(const F32vec4 &a)   { return _mm_acosh_ps(a);   }
	friend F32vec4 asin(const F32vec4 &a)    { return _mm_asin_ps(a);    }
	friend F32vec4 asinh(const F32vec4 &a)   { return _mm_asinh_ps(a);   }
	friend F32vec4 atan(const F32vec4 &a)    { return _mm_atan_ps(a);    }
	friend F32vec4 atan2(const F32vec4 &a, const F32vec4 &b) { return _mm_atan2_ps(a, b); }
	friend F32vec4 atanh(const F32vec4 &a)   { return _mm_atanh_ps(a);   }
	friend F32vec4 cbrt(const F32vec4 &a)    { return _mm_cbrt_ps(a);    }
	friend F32vec4 cos(const F32vec4 &a)     { return _mm_cos_ps(a);     }
	friend F32vec4 cosh(const F32vec4 &a)    { return _mm_cosh_ps(a);    }
	friend F32vec4 exp(const F32vec4 &a)     { return _mm_exp_ps(a);     }
	friend F32vec4 exp2(const F32vec4 &a)    { return _mm_exp2_ps(a);    }
	friend F32vec4 invcbrt(const F32vec4 &a) { return _mm_invcbrt_ps(a); }
	friend F32vec4 invsqrt(const F32vec4 &a) { return _mm_invsqrt_ps(a); }
	friend F32vec4 log(const F32vec4 &a)     { return _mm_log_ps(a);     }
	friend F32vec4 log10(const F32vec4 &a)   { return _mm_log10_ps(a);   }
	friend F32vec4 log2(const F32vec4 &a)    { return _mm_log2_ps(a);    }
	friend F32vec4 pow(const F32vec4 &a, const F32vec4 &b) { return _mm_pow_ps(a, b); }
	friend F32vec4 sin(const F32vec4 &a)     { return _mm_sin_ps(a);     }
	friend F32vec4 sinh(const F32vec4 &a)    { return _mm_sinh_ps(a);    }
	friend F32vec4 tan(const F32vec4 &a)     { return _mm_tan_ps(a);     }
	friend F32vec4 tanh(const F32vec4 &a)    { return _mm_tanh_ps(a);    }
	friend F32vec4 erf(const F32vec4 &a)     { return _mm_erf_ps(a);     }
	friend F32vec4 trunc(const F32vec4 &a)   { return _mm_trunc_ps(a);   }
	friend F32vec4 erfc(const F32vec4 &a)    { return _mm_erfc_ps(a);    }
	friend F32vec4 erfinv(const F32vec4 &a)  { return _mm_erfinv_ps(a);  }

	/* NewtonRaphson Reciprocal
	   [2 * rcpps(x) - (x * rcpps(x) * rcpps(x))] */
	friend F32vec4 rcp_nr(const F32vec4 &a)
	{
		F32vec4 Ra0 = _mm_rcp_ps(a);
		return _mm_sub_ps(_mm_add_ps(Ra0, Ra0), _mm_mul_ps(_mm_mul_ps(Ra0, a), Ra0));
	}

	/*	NewtonRaphson Reciprocal Square Root
	  	0.5 * rsqrtps * (3 - x * rsqrtps(x) * rsqrtps(x)) */
	friend F32vec4 rsqrt_nr(const F32vec4 &a)
	{
		static const F32vec4 fvecf0pt5(0.5f);
		static const F32vec4 fvecf3pt0(3.0f);
		F32vec4 Ra0 = _mm_rsqrt_ps(a);
		return (fvecf0pt5 * Ra0) * (fvecf3pt0 - (a * Ra0) * Ra0);

	}

	/* Compares: Mask is returned  */
	/* Macros expand to all compare intrinsics.  Example:
	friend F32vec4 cmpeq(const F32vec4 &a, const F32vec4 &b)
	{ return _mm_cmpeq_ps(a,b);} */
	#define Fvec32s4_COMP(op) \
	friend F32vec4 cmp##op (const F32vec4 &a, const F32vec4 &b) { return _mm_cmp##op##_ps(a,b); }
		Fvec32s4_COMP(eq)					// expanded to cmpeq(a,b)
		Fvec32s4_COMP(lt)					// expanded to cmplt(a,b)
		Fvec32s4_COMP(le)					// expanded to cmple(a,b)
		Fvec32s4_COMP(gt)					// expanded to cmpgt(a,b)
		Fvec32s4_COMP(ge)					// expanded to cmpge(a,b)
		Fvec32s4_COMP(neq)					// expanded to cmpneq(a,b)
		Fvec32s4_COMP(nlt)					// expanded to cmpnlt(a,b)
		Fvec32s4_COMP(nle)					// expanded to cmpnle(a,b)
		Fvec32s4_COMP(ngt)					// expanded to cmpngt(a,b)
		Fvec32s4_COMP(nge)					// expanded to cmpnge(a,b)
	#undef Fvec32s4_COMP

	/* Min and Max */
	friend F32vec4 simd_min(const F32vec4 &a, const F32vec4 &b) { return _mm_min_ps(a,b); }
	friend F32vec4 simd_max(const F32vec4 &a, const F32vec4 &b) { return _mm_max_ps(a,b); }

	/* Absolute value */
	friend F32vec4 abs(const F32vec4 &a)
        {
            return _mm_and_ps(a, _f32vec4_abs_mask);
        }

	/* Debug Features */
#if defined(FVEC_DEFINE_OUTPUT_OPERATORS)
	/* Output */
	friend FVEC_STD ostream & operator<<(FVEC_STD ostream & os,
                                         const F32vec4 &a) {
	/* To use: cout << "Elements of F32vec4 fvec are: " << fvec; */
	  float *fp = (float*)&a;
	  	os << "[3]:" << *(fp+3)
			<< " [2]:" << *(fp+2)
			<< " [1]:" << *(fp+1)
			<< " [0]:" << *fp;
		return os;
	}
#endif
	/* Element Access Only, no modifications to elements*/
	const float& operator[](int i) const {
		/* Assert enabled only during debug /DDEBUG */
		assert((0 <= i) && (i <= 3));			/* User should only access elements 0-3 */
		float *fp = (float*)&vec;
		return *(fp+i);
	}
	/* Element Access and Modification*/
	float& operator[](int i) {
		/* Assert enabled only during debug /DDEBUG */
		assert((0 <= i) && (i <= 3));			/* User should only access elements 0-3 */
		float *fp = (float*)&vec;
		return *(fp+i);
	}
};

						/* Miscellaneous */

/* Interleave low order data elements of a and b into destination */
inline F32vec4 unpack_low(const F32vec4 &a, const F32vec4 &b)
{ return _mm_unpacklo_ps(a, b); }

/* Interleave high order data elements of a and b into target */
inline F32vec4 unpack_high(const F32vec4 &a, const F32vec4 &b)
{ return _mm_unpackhi_ps(a, b); }

/* Move Mask to Integer returns 4 bit mask formed of most significant bits of a */
inline int move_mask(const F32vec4 &a)
{ return _mm_movemask_ps(a);}

						/* Data Motion Functions */

/* Load Unaligned loadu_ps: Unaligned */
inline void loadu(F32vec4 &a, float *p)
{ a = _mm_loadu_ps(p); }

/* Store Temporal storeu_ps: Unaligned */
inline void storeu(float *p, const F32vec4 &a)
{ _mm_storeu_ps(p, a); }

						/* Cacheability Support */

/* Non-Temporal Store */
inline void store_nta(float *p, const F32vec4 &a)
{ _mm_stream_ps(p,a);}

						/* Conditional Selects:*/
/*(a OP b)? c : d; where OP is any compare operator
Macros expand to conditional selects which use all compare intrinsics.
Example:
friend F32vec4 select_eq(const F32vec4 &a, const F32vec4 &b, const F32vec4 &c, const F32vec4 &d)
{
	F32vec4 mask = _mm_cmpeq_ps(a,b);
	return( (mask & c) | F32vec4((_mm_andnot_ps(mask,d))));
}
*/

#define Fvec32s4_SELECT(op) \
inline F32vec4 select_##op (const F32vec4 &a, const F32vec4 &b, const F32vec4 &c, const F32vec4 &d) 	   \
{																\
	F32vec4 mask = _mm_cmp##op##_ps(a,b);						\
	return( (mask & c) | F32vec4((_mm_andnot_ps(mask,d))));	\
}
Fvec32s4_SELECT(eq)			// generates select_eq(a,b)
Fvec32s4_SELECT(lt)			// generates select_lt(a,b)
Fvec32s4_SELECT(le)			// generates select_le(a,b)
Fvec32s4_SELECT(gt)			// generates select_gt(a,b)
Fvec32s4_SELECT(ge)			// generates select_ge(a,b)
Fvec32s4_SELECT(neq)		// generates select_neq(a,b)
Fvec32s4_SELECT(nlt)		// generates select_nlt(a,b)
Fvec32s4_SELECT(nle)		// generates select_nle(a,b)
Fvec32s4_SELECT(ngt)		// generates select_ngt(a,b)
Fvec32s4_SELECT(nge)		// generates select_nge(a,b)
#undef Fvec32s4_SELECT

/* Intel(R) Streaming SIMD Extensions Integer Intrinsics */

/* Max and Min */
inline Is16vec4 simd_max(const Is16vec4 &a, const Is16vec4 &b)		{ return _m_pmaxsw(a,b);}
inline Is16vec4 simd_min(const Is16vec4 &a, const Is16vec4 &b)		{ return _m_pminsw(a,b);}
inline Iu8vec8 simd_max(const Iu8vec8 &a, const Iu8vec8 &b)			{ return _m_pmaxub(a,b);}
inline Iu8vec8 simd_min(const Iu8vec8 &a, const Iu8vec8 &b)			{ return _m_pminub(a,b);}

/* Average */
inline Iu16vec4 simd_avg(const Iu16vec4 &a, const Iu16vec4 &b)	{ return _mm_avg_pu16(a,b); }
inline Iu8vec8 simd_avg(const Iu8vec8 &a, const Iu8vec8 &b)	{ return _mm_avg_pu8(a,b); }


/* Move ByteMask To Int: returns mask formed from most sig bits	of each vec of a */
inline int move_mask(const I8vec8 &a)								{ return _m_pmovmskb(a);}

/* Packed Multiply High Unsigned */
inline Iu16vec4 mul_high(const Iu16vec4 &a, const Iu16vec4 &b)		{ return _m_pmulhuw(a,b); }

/* Byte Mask Write: Write bytes if most significant bit in each corresponding byte is set */
inline void mask_move(const I8vec8 &a, const I8vec8 &b, char *addr)	{ _m_maskmovq(a, b, addr); }

/* Data Motion: Store Non Temporal */
inline void store_nta(__m64 *p, const M64 &a) { _mm_stream_pi(p,a); }

/* Conversions between ivec <-> fvec */

/* Convert first element of F32vec4 to int with truncation */
inline int F32vec4ToInt(const F32vec4 &a)
{
	return _mm_cvtt_ss2si(a);
}

/* Convert two lower SP FP values of a to Is32vec2 with truncation */
inline Is32vec2 F32vec4ToIs32vec2 (const F32vec4 &a)
{
	__m64 result;
	result = _mm_cvtt_ps2pi(a);
	return Is32vec2(result);
}

/* Convert the 32-bit int i to an SP FP value; the upper three SP FP values are passed through from a. */
inline F32vec4 IntToF32vec4(const F32vec4 &a, int i)
{
	__m128 result;
	result = _mm_cvt_si2ss(a,i);
	return F32vec4(result);
}

/* Convert the two 32-bit integer values in b to two SP FP values; the upper two SP FP values are passed from a. */
inline F32vec4 Is32vec2ToF32vec4(const F32vec4 &a, const Is32vec2 &b)
{
	__m128 result;
	result = _mm_cvt_pi2ps(a,b);
	return F32vec4(result);
}

class F32vec1
{
protected:
    __m128 vec;
public:

	/* Constructors: __m128, 1 float/double, 1 integer */

#ifdef FVEC_USE_CPP11_DEFAULTED_FUNCTIONS
    F32vec1() = default;
#else
	F32vec1() { vec = _mm_setzero_ps(); }
#endif

	F32vec1(int i)		{ vec = _mm_cvt_si2ss(vec,i);};

	/* Initialize each of 4 SP FPs with same float */
	EXPLICIT F32vec1(float f)	{ vec = _mm_set_ss(f); }

	/* Initialize each of 4 SP FPs with same float */
	EXPLICIT F32vec1(double d)	{ vec = _mm_set_ss((float) d); }

	/* initialize with __m128 data type */
	F32vec1(__m128 m)	{ vec = m; }

	/* Conversion functions */
	operator  __m128() const	{ return vec; }		/* Convert to float */

 	/* Logical Operators */
	friend F32vec1 operator &(const F32vec1 &a, const F32vec1 &b) { return _mm_and_ps(a,b); }
	friend F32vec1 operator |(const F32vec1 &a, const F32vec1 &b) { return _mm_or_ps(a,b); }
	friend F32vec1 operator ^(const F32vec1 &a, const F32vec1 &b) { return _mm_xor_ps(a,b); }

	/* Arithmetic Operators */
	friend F32vec1 operator +(const F32vec1 &a, const F32vec1 &b) { return _mm_add_ss(a,b); }
	friend F32vec1 operator -(const F32vec1 &a, const F32vec1 &b) { return _mm_sub_ss(a,b); }
	friend F32vec1 operator *(const F32vec1 &a, const F32vec1 &b) { return _mm_mul_ss(a,b); }
	friend F32vec1 operator /(const F32vec1 &a, const F32vec1 &b) { return _mm_div_ss(a,b); }

	F32vec1& operator +=(const F32vec1 &a)
                        { return *this = _mm_add_ss(vec,a); }
	F32vec1& operator -=(const F32vec1 &a)
                        { return *this = _mm_sub_ss(vec,a); }
	F32vec1& operator *=(const F32vec1 &a)
                        { return *this = _mm_mul_ss(vec,a); }
	F32vec1& operator /=(const F32vec1 &a)
                        { return *this = _mm_div_ss(vec,a); }
	F32vec1& operator &=(const F32vec1 &a)
                        { return *this = _mm_and_ps(vec,a); }
	F32vec1& operator |=(const F32vec1 &a)
                        { return *this = _mm_or_ps(vec,a); }
	F32vec1& operator ^=(const F32vec1 &a)
                        { return *this = _mm_xor_ps(vec,a); }

	/* Square Root */
	friend F32vec1 sqrt(const F32vec1 &a)	{ return _mm_sqrt_ss(a); }
	/* Reciprocal */
	friend F32vec1 rcp(const F32vec1 &a)	{ return _mm_rcp_ss(a); }
	/* Reciprocal Square Root */
	friend F32vec1 rsqrt(const F32vec1 &a)	{ return _mm_rsqrt_ss(a); }

	/* NewtonRaphson Reciprocal
	   [2 * rcpss(x) - (x * rcpss(x) * rcpss(x))] */
	friend F32vec1 rcp_nr(const F32vec1 &a)
	{
		F32vec1 Ra0 = _mm_rcp_ss(a);
		return _mm_sub_ss(_mm_add_ss(Ra0, Ra0), _mm_mul_ss(_mm_mul_ss(Ra0, a), Ra0));
	}

	/*	NewtonRaphson Reciprocal Square Root
	  	0.5 * rsqrtss * (3 - x * rsqrtss(x) * rsqrtss(x)) */
	friend F32vec1 rsqrt_nr(const F32vec1 &a)
	{
		static const F32vec1 fvecf0pt5(0.5f);
		static const F32vec1 fvecf3pt0(3.0f);
		F32vec1 Ra0 = _mm_rsqrt_ss(a);
		return (fvecf0pt5 * Ra0) * (fvecf3pt0 - (a * Ra0) * Ra0);
	}

	/* Compares: Mask is returned  */
	/* Macros expand to all compare intrinsics.  Example:
	friend F32vec1 cmpeq(const F32vec1 &a, const F32vec1 &b)
	{ return _mm_cmpeq_ss(a,b);} */
	#define Fvec32s1_COMP(op) \
	friend F32vec1 cmp##op (const F32vec1 &a, const F32vec1 &b) { return _mm_cmp##op##_ss(a,b); }
		Fvec32s1_COMP(eq)					// expanded to cmpeq(a,b)
		Fvec32s1_COMP(lt)					// expanded to cmplt(a,b)
		Fvec32s1_COMP(le)					// expanded to cmple(a,b)
		Fvec32s1_COMP(gt)					// expanded to cmpgt(a,b)
		Fvec32s1_COMP(ge)					// expanded to cmpge(a,b)
		Fvec32s1_COMP(neq)					// expanded to cmpneq(a,b)
		Fvec32s1_COMP(nlt)					// expanded to cmpnlt(a,b)
		Fvec32s1_COMP(nle)					// expanded to cmpnle(a,b)
		Fvec32s1_COMP(ngt)					// expanded to cmpngt(a,b)
		Fvec32s1_COMP(nge)					// expanded to cmpnge(a,b)
	#undef Fvec32s1_COMP

	/* Min and Max */
	friend F32vec1 simd_min(const F32vec1 &a, const F32vec1 &b) { return _mm_min_ss(a,b); }
	friend F32vec1 simd_max(const F32vec1 &a, const F32vec1 &b) { return _mm_max_ss(a,b); }

	/* Debug Features */
#if defined(FVEC_DEFINE_OUTPUT_OPERATORS)
	/* Output */
	friend FVEC_STD ostream & operator<<(FVEC_STD ostream & os,
                                         const F32vec1 &a) {
	/* To use: cout << "Elements of F32vec1 fvec are: " << fvec; */
	  float *fp = (float*)&a;
	  	os << "float:" << *fp;
		return os;
	}
#endif
};

						/* Conditional Selects:*/
/*(a OP b)? c : d; where OP is any compare operator
Macros expand to conditional selects which use all compare intrinsics.
Example:
friend F32vec1 select_eq(const F32vec1 &a, const F32vec1 &b, const F32vec1 &c, const F32vec1 &d)
{
	F32vec1 mask = _mm_cmpeq_ss(a,b);
	return( (mask & c) | F32vec1((_mm_andnot_ps(mask,d))));
}
*/

#define Fvec32s1_SELECT(op) \
inline F32vec1 select_##op (const F32vec1 &a, const F32vec1 &b, const F32vec1 &c, const F32vec1 &d) 	   \
{													   \
	F32vec1 mask = _mm_cmp##op##_ss(a,b);						                   \
	return( (mask & c) | F32vec1((_mm_andnot_ps(mask,d))));	                                           \
}
Fvec32s1_SELECT(eq)			// generates select_eq(a,b)
Fvec32s1_SELECT(lt)			// generates select_lt(a,b)
Fvec32s1_SELECT(le)			// generates select_le(a,b)
Fvec32s1_SELECT(gt)			// generates select_gt(a,b)
Fvec32s1_SELECT(ge)			// generates select_ge(a,b)
Fvec32s1_SELECT(neq)		// generates select_neq(a,b)
Fvec32s1_SELECT(nlt)		// generates select_nlt(a,b)
Fvec32s1_SELECT(nle)		// generates select_nle(a,b)
Fvec32s1_SELECT(ngt)		// generates select_ngt(a,b)
Fvec32s1_SELECT(nge)		// generates select_nge(a,b)
#undef Fvec32s1_SELECT

/* Conversions between ivec <-> fvec */

/* Convert F32vec1 to int */
inline int F32vec1ToInt(const F32vec1 &a)
{
	return _mm_cvtt_ss2si(a);
}

#undef FVEC_DEFINE_OUTPUT_OPERATORS
#undef FVEC_STD

#ifdef FVEC_USE_CPP11_DEFAULTED_FUNCTIONS
#undef FVEC_USE_CPP11_DEFAULTED_FUNCTIONS
#endif

#pragma pack(pop) /* 16-B aligned */
#endif /* FVEC_H_INCLUDED */
