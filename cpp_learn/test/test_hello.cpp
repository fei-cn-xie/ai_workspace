#include "hello/hello.h"

#include "gtest/gtest.h"

class HelloTest : public ::testing::Test {
public:
    void SetUp() override {
        // 在每个测试用例之前执行的代码
    }

    void TearDown() override {
        // 在每个测试用例之后执行的代码
    }
};

TEST_F(HelloTest, Hello1) {
    EXPECT_EQ(0, Hello());
}

TEST_F(HelloTest, Hello2) {
    EXPECT_EQ(152, Hello_Fei());
}

TEST(Hello, Hello3) {
    EXPECT_EQ(0, Hello());
}