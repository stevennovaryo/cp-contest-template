#include <bits/stdc++.h>
#include <tcframe/spec.hpp>

using namespace std;
using namespace tcframe;

const int MAXA = 1000000000;

class ProblemSpec : public BaseProblemSpec {
 protected:
  int A, B;
  int ans;

  void InputFormat() {
    LINE(A, B);
  }

  void OutputFormat() {
    LINE(ans);
  }

  void GradingConfig() {
    TimeLimit(1);
    MemoryLimit(64);
  }

  void Constraints() {
    CONS(1 <= A && A <= MAXA);
    CONS(1 <= B && B <= MAXA);
  }
};

class TestSpec : public BaseTestSpec<ProblemSpec> {
protected:
  void SampleTestCase1() {
    Input({
      "1 1",
    });
    Output({
      "2",
    });
  }

  void SampleTestCase2() {
    Input({
      "3 2",
    });
    Output({
      "5",
    });
  }

  void SampleTestCase3() {
    Input({
      "32 68",
    });
    Output({
      "100",
    });
  }

  void SampleTestCase4() {
    Input({
      "5 1008",
    });
    Output({
      "4",
    });
  }

  void TestGroup1() {
    CASE(A = 2; B = 1009);
    CASE(A = 5; B = 1010);
    CASE(A = 4; B = 999919); // 1009 | B
    CASE(A = 573; B = 10); // ans = 0
    CASE(A = 205; B = 500); // ans = 1008
    CASE(A = MAXA; B = MAXA); // max test
    CASE(A = MAXA-1; B = MAXA-1);
  }
};
