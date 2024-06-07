

add_cython_target(soft_dtw_fast CXX)
add_library(soft_dtw_fast MODULE ${soft_dtw_fast})
python_extension_module(soft_dtw_fast)

install(TARGETS soft_dtw_fast LIBRARY DESTINATION soft-dtw)
