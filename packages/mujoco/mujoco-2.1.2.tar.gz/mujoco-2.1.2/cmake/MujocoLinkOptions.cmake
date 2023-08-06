include(CheckCSourceCompiles)

# Gets the appropriate linker options for building MuJoCo, based on features available on the
# linker.
function(get_mujoco_extra_link_options OUTPUT_VAR)
  if(MSVC)
    set(EXTRA_LINK_OPTIONS /OPT:REF /OPT:ICF=5)
  else()
    set(EXTRA_LINK_OPTIONS)

    if(WIN32)
      set(CMAKE_REQUIRED_FLAGS "-fuse-ld=lld-link")
      check_c_source_compiles("int main() {}" SUPPORTS_LLD)
      if(SUPPORTS_LLD)
        set(EXTRA_LINK_OPTIONS
            ${EXTRA_LINK_OPTIONS}
            -fuse-ld=lld-link
            -Wl,/OPT:REF
            -Wl,/OPT:ICF
        )
      endif()
    else()
      set(CMAKE_REQUIRED_FLAGS "-fuse-ld=lld")
      check_c_source_compiles("int main() {}" SUPPORTS_LLD)
      if(SUPPORTS_LLD)
        set(EXTRA_LINK_OPTIONS ${EXTRA_LINK_OPTIONS} -fuse-ld=lld)
      else()
        set(CMAKE_REQUIRED_FLAGS "-fuse-ld=gold")
        check_c_source_compiles("int main() {}" SUPPORTS_GOLD)
        if(SUPPORTS_GOLD)
          set(EXTRA_LINK_OPTIONS ${EXTRA_LINK_OPTIONS} -fuse-ld=gold)
        endif()
      endif()

      set(CMAKE_REQUIRED_FLAGS ${EXTRA_LINK_OPTIONS} "-Wl,--gc-sections")
      check_c_source_compiles("int main() {}" SUPPORTS_GC_SECTIONS)
      if(SUPPORTS_GC_SECTIONS)
        set(EXTRA_LINK_OPTIONS ${EXTRA_LINK_OPTIONS} -Wl,--gc-sections)
      else()
        set(CMAKE_REQUIRED_FLAGS ${EXTRA_LINK_OPTIONS} "-Wl,-dead_strip")
        check_c_source_compiles("int main() {}" SUPPORTS_DEAD_STRIP)
        if(SUPPORTS_DEAD_STRIP)
          set(EXTRA_LINK_OPTIONS ${EXTRA_LINK_OPTIONS} -Wl,-dead_strip)
        endif()
      endif()
    endif()
  endif()

  set("${OUTPUT_VAR}"
      ${EXTRA_LINK_OPTIONS}
      PARENT_SCOPE
  )
endfunction()
