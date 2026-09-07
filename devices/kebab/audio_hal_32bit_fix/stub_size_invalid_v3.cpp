#include <cstdint>

namespace android {
namespace ui {

class Size {
public:
    int32_t width = -1;
    int32_t height = -1;
    static const Size INVALID __attribute__((visibility("default")));
};

__attribute__((used, visibility("default")))
const Size Size::INVALID{};

} // namespace ui

class HdrCapabilities {
public:
    ~HdrCapabilities();
};

__attribute__((used, visibility("default")))
HdrCapabilities::~HdrCapabilities() {}

} // namespace android

// vendor::oplus::hardware::extcamera::V1_0::IExtCameraCallback::interfaceChain
// -- see explanation above; forced via asm() to bypass C++ mangling
// convention differences (bionic uses libc++'s std::__1 namespace).
extern "C" __attribute__((visibility("default")))
void _extcamera_interfacechain_stub(void*, void*)
    asm("_ZN6vendor5oplus8hardware9extcamera4V1_018IExtCameraCallback14interfaceChainENSt3__18functionIFvRKN7android8hardware8hidl_vecINS8_11hidl_stringEEEEEE");

void _extcamera_interfacechain_stub(void* /*self*/, void* /*cb_holder*/) {
    // Intentional no-op -- see explanation in the original stub file.
}
