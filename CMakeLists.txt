cmake_minimum_required(VERSION 2.8.12)
project(conan-osip)

## Conan Setup #################################################################
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

## General settings ############################################################
set(OSIP_VERSION_MAJOR 5)
set(OSIP_VERSION_MINOR 0)
set(OSIP_VERSION_PATCH 0)

set(WINDOWS_EXPORT_ALL_SYMBOLS TRUE)

find_package(Threads)

## Build oSIP2 library #########################################################
set(OSIP_TARGET osip2)
set(OSIP_SOURCE_FILES ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osip2/fsm_misc.c
                      ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osip2/ict.c
                      ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osip2/ict_fsm.c
                      ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osip2/ist.c
                      ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osip2/ist_fsm.c
                      ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osip2/nict.c
                      ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osip2/nict_fsm.c
                      ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osip2/nist.c
                      ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osip2/nist_fsm.c
                      ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osip2/osip.c
                      ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osip2/osip_dialog.c
                      ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osip2/osip_event.c
                      ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osip2/osip_time.c
                      ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osip2/osip_transaction.c
                      ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osip2/port_condv.c
                      ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osip2/port_fifo.c
                      ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osip2/port_sema.c
                      ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osip2/port_thread.c
                      ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osip2/fsm.h
                      ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/include/osip2/internal.h
                      ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/include/osip2/osip.h
                      ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/include/osip2/osip_condv.h
                      ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/include/osip2/osip_dialog.h
                      ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/include/osip2/osip_fifo.h
                      ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/include/osip2/osip_mt.h
                      ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osip2/xixt.h)

add_library(${OSIP_TARGET} ${OSIP_SOURCE_FILES})
target_link_libraries(${OSIP_TARGET} ${CONAN_LIBS} ${CMAKE_THREAD_LIBS_INIT})
target_include_directories(${OSIP_TARGET} PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/include)
set_property(TARGET ${OSIP_TARGET} PROPERTY C_STANDARD 99)

## Build oSIP Parser 2 #########################################################
set(OSIPPARSER_TARGET osipparser2)
set(OSIPPARSER_SOURCE_FILES ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osipparser2/osip_accept.c
                            ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osipparser2/osip_accept_encoding.c
                            ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osipparser2/osip_accept_language.c
                            ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osipparser2/osip_alert_info.c
                            ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osipparser2/osip_allow.c
                            ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osipparser2/osip_authentication_info.c
                            ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osipparser2/osip_authorization.c
                            ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osipparser2/osip_body.c
                            ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osipparser2/osip_call_id.c
                            ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osipparser2/osip_call_info.c
                            ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osipparser2/osip_contact.c
                            ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osipparser2/osip_content_disposition.c
                            ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osipparser2/osip_content_encoding.c
                            ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osipparser2/osip_content_length.c
                            ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osipparser2/osip_content_type.c
                            ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osipparser2/osip_cseq.c
                            ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osipparser2/osip_error_info.c
                            ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osipparser2/osip_from.c
                            ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osipparser2/osip_header.c
                            ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osipparser2/osip_list.c
                            ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osipparser2/osip_md5c.c
                            ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osipparser2/osip_message.c
                            ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osipparser2/osip_message_parse.c
                            ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osipparser2/osip_message_to_str.c
                            ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osipparser2/osip_mime_version.c
                            ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osipparser2/osip_parser_cfg.c
                            ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osipparser2/osip_port.c
                            ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osipparser2/osip_proxy_authenticate.c
                            ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osipparser2/osip_proxy_authentication_info.c
                            ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osipparser2/osip_proxy_authorization.c
                            ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osipparser2/osip_record_route.c
                            ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osipparser2/osip_route.c
                            ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osipparser2/osip_to.c
                            ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osipparser2/osip_uri.c
                            ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osipparser2/osip_via.c
                            ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osipparser2/osip_www_authenticate.c
                            ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osipparser2/sdp_accessor.c
                            ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/osipparser2/sdp_message.c)

add_library(${OSIPPARSER_TARGET} ${OSIPPARSER_SOURCE_FILES})
target_link_libraries(${OSIPPARSER_TARGET} ${CONAN_LIBS})
target_include_directories(${OSIPPARSER_TARGET} PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/include)

# Install ######################################################################
install(TARGETS ${OSIP_TARGET}
        RUNTIME DESTINATION bin
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib)

install(TARGETS ${OSIPPARSER_TARGET}
        RUNTIME DESTINATION bin
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib)

install(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/include
        DESTINATION ${CMAKE_INSTALL_PREFIX})
