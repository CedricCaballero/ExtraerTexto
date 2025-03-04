! <copyright>
!
!     Copyright (C) 1985 Intel Corporation.
!
!     This software and the related documents are Intel copyrighted materials,
!     and your use of them is governed by the express license under which they
!     were provided to you ("License"). Unless the License provides otherwise,
!     you may not use, modify, copy, publish, distribute, disclose or transmit
!     this software or the related documents without Intel's prior written permission.
!
!     This software and the related documents are provided as is, with no express or
!     implied warranties, other than those that are expressly stated in the License.
!
! </copyright>

      integer omp_integer_kind
      parameter(omp_integer_kind=4)
      integer omp_logical_kind
      parameter(omp_logical_kind=4)
      integer omp_real_kind
      parameter(omp_real_kind=4)
      integer omp_lock_kind
      parameter(omp_lock_kind=int_ptr_kind())
      integer omp_nest_lock_kind
      parameter(omp_nest_lock_kind=int_ptr_kind())
      integer omp_sched_kind
      parameter(omp_sched_kind=omp_integer_kind)
      integer omp_proc_bind_kind
      parameter(omp_proc_bind_kind=omp_integer_kind)
      integer kmp_pointer_kind
      parameter(kmp_pointer_kind=int_ptr_kind())
      integer kmp_size_t_kind
      parameter(kmp_size_t_kind=int_ptr_kind())
      integer kmp_affinity_mask_kind
      parameter(kmp_affinity_mask_kind=int_ptr_kind())
      integer omp_sync_hint_kind
      parameter(omp_sync_hint_kind=omp_integer_kind)
      integer omp_lock_hint_kind
      parameter(omp_lock_hint_kind=omp_sync_hint_kind)
      integer omp_control_tool_kind
      parameter(omp_control_tool_kind=omp_integer_kind)
      integer omp_control_tool_result_kind
      parameter(omp_control_tool_result_kind=omp_integer_kind)
      integer omp_allocator_handle_kind
      parameter(omp_allocator_handle_kind=int_ptr_kind())
      integer omp_memspace_handle_kind
      parameter(omp_memspace_handle_kind=int_ptr_kind())
      integer omp_alloctrait_key_kind
      parameter(omp_alloctrait_key_kind=omp_integer_kind)
      integer omp_alloctrait_val_kind
      parameter(omp_alloctrait_val_kind=int_ptr_kind())
      integer omp_pause_resource_kind
      parameter(omp_pause_resource_kind=omp_integer_kind)
      integer omp_depend_kind
      parameter(omp_depend_kind=int_ptr_kind())
      integer omp_event_handle_kind
      parameter(omp_event_handle_kind=int_ptr_kind())
      integer omp_interop_kind
      parameter(omp_interop_kind=int_ptr_kind())
      integer omp_interop_fr_kind
      parameter(omp_interop_fr_kind=omp_integer_kind)

      integer(kind=omp_integer_kind)openmp_version
      parameter(openmp_version=202111)
      integer(kind=omp_integer_kind)kmp_version_major
      parameter(kmp_version_major=5)
      integer(kind=omp_integer_kind)kmp_version_minor
      parameter(kmp_version_minor=0)
      integer(kind=omp_integer_kind)kmp_version_build
      parameter(kmp_version_build=20240820)
      character(*)kmp_build_date
      parameter(kmp_build_date='2024-08-20 16-01-09 UTC')

      integer(kind=omp_sched_kind)omp_sched_static
      parameter(omp_sched_static=1)
      integer(kind=omp_sched_kind)omp_sched_dynamic
      parameter(omp_sched_dynamic=2)
      integer(kind=omp_sched_kind)omp_sched_guided
      parameter(omp_sched_guided=3)
      integer(kind=omp_sched_kind)omp_sched_auto
      parameter(omp_sched_auto=4)
      integer(kind=omp_sched_kind)omp_sched_monotonic
      parameter(omp_sched_monotonic=Z'80000000')

      integer(kind=omp_proc_bind_kind)omp_proc_bind_false
      parameter(omp_proc_bind_false=0)
      integer(kind=omp_proc_bind_kind)omp_proc_bind_true
      parameter(omp_proc_bind_true=1)
      integer(kind=omp_proc_bind_kind)omp_proc_bind_master
      parameter(omp_proc_bind_master=2)
      integer(kind=omp_proc_bind_kind)omp_proc_bind_close
      parameter(omp_proc_bind_close=3)
      integer(kind=omp_proc_bind_kind)omp_proc_bind_spread
      parameter(omp_proc_bind_spread=4)

      integer(kind=omp_sync_hint_kind)omp_sync_hint_none
      parameter(omp_sync_hint_none=0)
      integer(kind=omp_sync_hint_kind)omp_sync_hint_uncontended
      parameter(omp_sync_hint_uncontended=1)
      integer(kind=omp_sync_hint_kind)omp_sync_hint_contended
      parameter(omp_sync_hint_contended=2)
      integer(kind=omp_sync_hint_kind)omp_sync_hint_nonspeculative
      parameter(omp_sync_hint_nonspeculative=4)
      integer(kind=omp_sync_hint_kind)omp_sync_hint_speculative
      parameter(omp_sync_hint_speculative=8)
      integer(kind=omp_lock_hint_kind)omp_lock_hint_none
      parameter(omp_lock_hint_none=omp_sync_hint_none)
      integer(kind=omp_lock_hint_kind)omp_lock_hint_uncontended
      parameter(omp_lock_hint_uncontended=omp_sync_hint_uncontended)
      integer(kind=omp_lock_hint_kind)omp_lock_hint_contended
      parameter(omp_lock_hint_contended=omp_sync_hint_contended)
      integer(kind=omp_lock_hint_kind)omp_lock_hint_nonspeculative
      parameter(omp_lock_hint_nonspeculative=4)
      integer(kind=omp_lock_hint_kind)omp_lock_hint_speculative
      parameter(omp_lock_hint_speculative=omp_sync_hint_speculative)
      integer(kind=omp_lock_hint_kind)kmp_lock_hint_hle
      parameter(kmp_lock_hint_hle=65536)
      integer(kind=omp_lock_hint_kind)kmp_lock_hint_rtm
      parameter(kmp_lock_hint_rtm=131072)
      integer(kind=omp_lock_hint_kind)kmp_lock_hint_adaptive
      parameter(kmp_lock_hint_adaptive=262144)

      integer(kind=omp_control_tool_kind)omp_control_tool_start
      parameter(omp_control_tool_start=1)
      integer(kind=omp_control_tool_kind)omp_control_tool_pause
      parameter(omp_control_tool_pause=2)
      integer(kind=omp_control_tool_kind)omp_control_tool_flush
      parameter(omp_control_tool_flush=3)
      integer(kind=omp_control_tool_kind)omp_control_tool_end
      parameter(omp_control_tool_end=4)

      integer(omp_control_tool_result_kind)omp_control_tool_notool
      parameter(omp_control_tool_notool=-2)
      integer(omp_control_tool_result_kind)omp_control_tool_nocallback
      parameter(omp_control_tool_nocallback=-1)
      integer(omp_control_tool_result_kind)omp_control_tool_success
      parameter(omp_control_tool_success=0)
      integer(omp_control_tool_result_kind)omp_control_tool_ignored
      parameter(omp_control_tool_ignored=1)

      integer(kind=omp_alloctrait_key_kind)omp_atk_sync_hint
      parameter(omp_atk_sync_hint=1)
      integer(kind=omp_alloctrait_key_kind)omp_atk_alignment
      parameter(omp_atk_alignment=2)
      integer(kind=omp_alloctrait_key_kind)omp_atk_access
      parameter(omp_atk_access=3)
      integer(kind=omp_alloctrait_key_kind)omp_atk_pool_size
      parameter(omp_atk_pool_size=4)
      integer(kind=omp_alloctrait_key_kind)omp_atk_fallback
      parameter(omp_atk_fallback=5)
      integer(kind=omp_alloctrait_key_kind)omp_atk_fb_data
      parameter(omp_atk_fb_data=6)
      integer(kind=omp_alloctrait_key_kind)omp_atk_pinned
      parameter(omp_atk_pinned=7)
      integer(kind=omp_alloctrait_key_kind)omp_atk_partition
      parameter(omp_atk_partition=8)
      integer(kind=omp_alloctrait_key_kind)omp_atk_pin_device
      parameter(omp_atk_pin_device=9)
      integer(kind=omp_alloctrait_key_kind)omp_atk_preferred_device
      parameter(omp_atk_preferred_device=10)
      integer(kind=omp_alloctrait_key_kind)omp_atk_device_access
      parameter(omp_atk_device_access=11)
      integer(kind=omp_alloctrait_key_kind)omp_atk_target_access
      parameter(omp_atk_target_access=12)
      integer(kind=omp_alloctrait_key_kind)omp_atk_atomic_scope
      parameter(omp_atk_atomic_scope=13)
      integer(kind=omp_alloctrait_key_kind)omp_atk_part_size
      parameter(omp_atk_part_size=14)

      integer(kind=omp_alloctrait_val_kind)omp_atv_default
      parameter(omp_atv_default=-1)
!     Reserved for future use
      integer(kind=omp_alloctrait_val_kind)omp_atv_false
      parameter(omp_atv_false=0)
!     Reserved for future use
      integer(kind=omp_alloctrait_val_kind)omp_atv_true
      parameter(omp_atv_true=1)
      integer(kind=omp_alloctrait_val_kind)omp_atv_contended
      parameter(omp_atv_contended=3)
      integer(kind=omp_alloctrait_val_kind)omp_atv_uncontended
      parameter(omp_atv_uncontended=4)
      integer(kind=omp_alloctrait_val_kind)omp_atv_serialized
      parameter(omp_atv_serialized=5)
      integer(kind=omp_alloctrait_val_kind)omp_atv_sequential
      parameter(omp_atv_sequential=5)
      integer(kind=omp_alloctrait_val_kind)omp_atv_private
      parameter(omp_atv_private=6)
      integer(kind=omp_alloctrait_val_kind)omp_atv_device
      parameter(omp_atv_device=7)
      integer(kind=omp_alloctrait_val_kind)omp_atv_thread
      parameter(omp_atv_thread=8)
      integer(kind=omp_alloctrait_val_kind)omp_atv_pteam
      parameter(omp_atv_pteam=9)
      integer(kind=omp_alloctrait_val_kind)omp_atv_cgroup
      parameter(omp_atv_cgroup=10)
      integer(kind=omp_alloctrait_val_kind)omp_atv_default_mem_fb
      parameter(omp_atv_default_mem_fb=11)
      integer(kind=omp_alloctrait_val_kind)omp_atv_null_fb
      parameter(omp_atv_null_fb=12)
      integer(kind=omp_alloctrait_val_kind)omp_atv_abort_fb
      parameter(omp_atv_abort_fb=13)
      integer(kind=omp_alloctrait_val_kind)omp_atv_allocator_fb
      parameter(omp_atv_allocator_fb=14)
      integer(kind=omp_alloctrait_val_kind)omp_atv_environment
      parameter(omp_atv_environment=15)
      integer(kind=omp_alloctrait_val_kind)omp_atv_nearest
      parameter(omp_atv_nearest=16)
      integer(kind=omp_alloctrait_val_kind)omp_atv_blocked
      parameter(omp_atv_blocked=17)
      integer(kind=omp_alloctrait_val_kind)omp_atv_interleaved
      parameter(omp_atv_interleaved=18)
      integer(kind=omp_alloctrait_val_kind)omp_atv_all
      parameter(omp_atv_all=19)
      integer(kind=omp_alloctrait_val_kind)omp_atv_single
      parameter(omp_atv_single=20)
      integer(kind=omp_alloctrait_val_kind)omp_atv_multiple
      parameter(omp_atv_multiple=21)
      integer(kind=omp_alloctrait_val_kind)omp_atv_memspace
      parameter(omp_atv_memspace=22)

      type omp_alloctrait
        integer (kind=omp_alloctrait_key_kind) key
        integer (kind=omp_alloctrait_val_kind) value
      end type omp_alloctrait

      integer(kind=omp_allocator_handle_kind)omp_null_allocator
      parameter(omp_null_allocator=0)
      integer(kind=omp_allocator_handle_kind)omp_default_mem_alloc
      parameter(omp_default_mem_alloc=1)
      integer(kind=omp_allocator_handle_kind)omp_large_cap_mem_alloc
      parameter(omp_large_cap_mem_alloc=2)
      integer(kind=omp_allocator_handle_kind)omp_const_mem_alloc
      parameter(omp_const_mem_alloc=3)
      integer(kind=omp_allocator_handle_kind)omp_high_bw_mem_alloc
      parameter(omp_high_bw_mem_alloc=4)
      integer(kind=omp_allocator_handle_kind)omp_low_lat_mem_alloc
      parameter(omp_low_lat_mem_alloc=5)
      integer(kind=omp_allocator_handle_kind)omp_cgroup_mem_alloc
      parameter(omp_cgroup_mem_alloc=6)
      integer(kind=omp_allocator_handle_kind)omp_pteam_mem_alloc
      parameter(omp_pteam_mem_alloc=7)
      integer(kind=omp_allocator_handle_kind)omp_thread_mem_alloc
      parameter(omp_thread_mem_alloc=8)
      integer(omp_allocator_handle_kind)llvm_omp_target_host_mem_alloc
      parameter(llvm_omp_target_host_mem_alloc=100)
      integer(omp_allocator_handle_kind)llvm_omp_target_shared_mem_alloc
      parameter(llvm_omp_target_shared_mem_alloc=101)
      integer(omp_allocator_handle_kind)llvm_omp_target_device_mem_alloc
      parameter(llvm_omp_target_device_mem_alloc=102)
      integer(omp_allocator_handle_kind)omp_target_host_mem_alloc
      parameter(omp_target_host_mem_alloc=100)
      integer(omp_allocator_handle_kind)omp_target_shared_mem_alloc
      parameter(omp_target_shared_mem_alloc=101)
      integer(omp_allocator_handle_kind)omp_target_device_mem_alloc
      parameter(omp_target_device_mem_alloc=102)

      integer(kind=omp_memspace_handle_kind)omp_null_mem_space
      parameter(omp_null_mem_space=0)
      integer(kind=omp_memspace_handle_kind)omp_default_mem_space
      parameter(omp_default_mem_space=99)
      integer(kind=omp_memspace_handle_kind)omp_large_cap_mem_space
      parameter(omp_large_cap_mem_space=1)
      integer(kind=omp_memspace_handle_kind)omp_const_mem_space
      parameter(omp_const_mem_space=2)
      integer(kind=omp_memspace_handle_kind)omp_high_bw_mem_space
      parameter(omp_high_bw_mem_space=3)
      integer(kind=omp_memspace_handle_kind)omp_low_lat_mem_space
      parameter(omp_low_lat_mem_space=4)
      integer(omp_memspace_handle_kind)llvm_omp_target_host_mem_space
      parameter(llvm_omp_target_host_mem_space=100)
      integer(omp_memspace_handle_kind)llvm_omp_target_shared_mem_space
      parameter(llvm_omp_target_shared_mem_space=101)
      integer(omp_memspace_handle_kind)llvm_omp_target_device_mem_space
      parameter(llvm_omp_target_device_mem_space=102)
      integer(omp_memspace_handle_kind)omp_target_host_mem_space
      parameter(omp_target_host_mem_space=100)
      integer(omp_memspace_handle_kind)omp_target_shared_mem_space
      parameter(omp_target_shared_mem_space=101)
      integer(omp_memspace_handle_kind)omp_target_device_mem_space
      parameter(omp_target_device_mem_space=102)

      integer(kind=omp_pause_resource_kind)omp_pause_resume
      parameter(omp_pause_resume=0)
      integer(kind=omp_pause_resource_kind)omp_pause_soft
      parameter(omp_pause_soft=1)
      integer(kind=omp_pause_resource_kind)omp_pause_hard
      parameter(omp_pause_hard=2)
      integer(kind=omp_pause_resource_kind)omp_pause_stop_tool
      parameter(omp_pause_stop_tool=3)

      integer(kind=omp_interop_fr_kind)omp_ifr_cuda
      parameter(omp_ifr_cuda=1)
      integer(kind=omp_interop_fr_kind)omp_ifr_cuda_driver
      parameter(omp_ifr_cuda_driver=2)
      integer(kind=omp_interop_fr_kind)omp_ifr_opencl
      parameter(omp_ifr_opencl=3)
      integer(kind=omp_interop_fr_kind)omp_ifr_sycl
      parameter(omp_ifr_sycl=4)
      integer(kind=omp_interop_fr_kind)omp_ifr_hip
      parameter(omp_ifr_hip=5)
      integer(kind=omp_interop_fr_kind)omp_ifr_level_zero
      parameter(omp_ifr_level_zero=6)
      integer(kind=omp_interop_fr_kind)omp_ifr_unified_runtime
      parameter(omp_ifr_unified_runtime=7)
      integer(kind=omp_interop_fr_kind)omp_ifr_last
      parameter(omp_ifr_last=8)

      integer(kind=omp_interop_kind)omp_interop_none
      parameter(omp_interop_none=0)

      integer(kind=omp_integer_kind)omp_initial_device
      parameter(omp_initial_device=-1)
      integer(kind=omp_integer_kind)omp_invalid_device
      parameter(omp_invalid_device=-10)

      ! target shared allocation hint
      integer(kind=omp_integer_kind)ompx_mem_hint_read_mostly
      parameter(ompx_mem_hint_read_mostly=0)
      integer(kind=omp_integer_kind)ompx_mem_hint_prefer_device
      parameter(ompx_mem_hint_prefer_device=2)
      integer(kind=omp_integer_kind)ompx_mem_hint_non_atomic_mostly
      parameter(ompx_mem_hint_non_atomic_mostly=4)
      integer(kind=omp_integer_kind)ompx_mem_hint_cached
      parameter(ompx_mem_hint_cached=6)
      integer(kind=omp_integer_kind)ompx_mem_hint_uncached
      parameter(ompx_mem_hint_uncached=7)
      integer(kind=omp_integer_kind)ompx_mem_hint_prefer_host
      parameter(ompx_mem_hint_prefer_host=8)
      integer(kind=omp_integer_kind)ompx_mem_hint_device_access_mostly
      parameter(ompx_mem_hint_device_access_mostly=9)
      integer(kind=omp_integer_kind)ompx_mem_hint_host_access_mostly
      parameter(ompx_mem_hint_host_access_mostly=10)
      integer(kind=omp_integer_kind)ompx_mem_hint_non_coherent
      parameter(ompx_mem_hint_non_coherent=11)
      integer(kind=omp_integer_kind)ompx_mem_hint_none
      parameter(ompx_mem_hint_none=-1)

      ! free-agent thread num value (must be less than -1)
      integer(kind=omp_integer_kind)omp_unassigned_thread
      parameter(omp_unassigned_thread=-2)

      interface

!       ***
!       *** omp_* entry points
!       ***

        subroutine omp_set_num_threads(num_threads) bind(c)
          import
          integer (kind=omp_integer_kind), value :: num_threads
        end subroutine omp_set_num_threads

        subroutine omp_set_dynamic(dynamic_threads) bind(c)
          import
          logical (kind=omp_logical_kind), value :: dynamic_threads
        end subroutine omp_set_dynamic

        subroutine omp_set_nested(nested) bind(c)
          import
          logical (kind=omp_logical_kind), value :: nested
        end subroutine omp_set_nested

        function omp_get_num_threads() bind(c)
          import
          integer (kind=omp_integer_kind) omp_get_num_threads
        end function omp_get_num_threads

        function omp_get_max_threads() bind(c)
          import
          integer (kind=omp_integer_kind) omp_get_max_threads
        end function omp_get_max_threads

        function omp_get_thread_num() bind(c)
          import
          integer (kind=omp_integer_kind) omp_get_thread_num
        end function omp_get_thread_num

        function omp_get_num_procs() bind(c)
          import
          integer (kind=omp_integer_kind) omp_get_num_procs
        end function omp_get_num_procs

        function omp_in_parallel() bind(c)
          import
          logical (kind=omp_logical_kind) omp_in_parallel
        end function omp_in_parallel

        function omp_in_final() bind(c)
          import
          logical (kind=omp_logical_kind) omp_in_final
        end function omp_in_final

        function omp_get_dynamic() bind(c)
          import
          logical (kind=omp_logical_kind) omp_get_dynamic
        end function omp_get_dynamic

        function omp_get_nested() bind(c)
          import
          logical (kind=omp_logical_kind) omp_get_nested
        end function omp_get_nested

        function omp_get_thread_limit() bind(c)
          import
          integer (kind=omp_integer_kind) omp_get_thread_limit
        end function omp_get_thread_limit

        subroutine omp_set_max_active_levels(max_levels) bind(c)
          import
          integer (kind=omp_integer_kind), value :: max_levels
        end subroutine omp_set_max_active_levels

        function omp_get_max_active_levels() bind(c)
          import
          integer (kind=omp_integer_kind) omp_get_max_active_levels
        end function omp_get_max_active_levels

        function omp_get_level() bind(c)
          import
          integer (kind=omp_integer_kind) omp_get_level
        end function omp_get_level

        function omp_get_active_level() bind(c)
          import
          integer (kind=omp_integer_kind) omp_get_active_level
        end function omp_get_active_level

        function omp_get_ancestor_thread_num(level) bind(c)
          import
          integer (kind=omp_integer_kind) omp_get_ancestor_thread_num
          integer (kind=omp_integer_kind), value :: level
        end function omp_get_ancestor_thread_num

        function omp_get_team_size(level) bind(c)
          import
          integer (kind=omp_integer_kind) omp_get_team_size
          integer (kind=omp_integer_kind), value :: level
        end function omp_get_team_size

        subroutine omp_set_schedule(kind, chunk_size) bind(c)
          import
          integer (kind=omp_sched_kind), value :: kind
          integer (kind=omp_integer_kind), value :: chunk_size
        end subroutine omp_set_schedule

        subroutine omp_get_schedule(kind, chunk_size) bind(c)
          import
          integer (kind=omp_sched_kind) kind
          integer (kind=omp_integer_kind) chunk_size
        end subroutine omp_get_schedule

        function omp_get_proc_bind() bind(c)
          import
          integer (kind=omp_proc_bind_kind) omp_get_proc_bind
        end function omp_get_proc_bind

        function omp_get_num_places() bind(c)
          import
          integer (kind=omp_integer_kind) omp_get_num_places
        end function omp_get_num_places

        function omp_get_place_num_procs(place_num) bind(c)
          import
          integer (kind=omp_integer_kind), value :: place_num
          integer (kind=omp_integer_kind) omp_get_place_num_procs
        end function omp_get_place_num_procs

        subroutine omp_get_place_proc_ids(place_num, ids) bind(c)
          import
          integer (kind=omp_integer_kind), value :: place_num
          integer (kind=omp_integer_kind) ids(*)
        end subroutine omp_get_place_proc_ids

        function omp_get_place_num() bind(c)
          import
          integer (kind=omp_integer_kind) omp_get_place_num
        end function omp_get_place_num

        function omp_get_partition_num_places() bind(c)
          import
          integer (kind=omp_integer_kind) omp_get_partition_num_places
        end function omp_get_partition_num_places

        subroutine omp_get_partition_place_nums(place_nums) bind(c)
          import
          integer (kind=omp_integer_kind) place_nums(*)
        end subroutine omp_get_partition_place_nums

        function omp_get_wtime() bind(c)
          double precision omp_get_wtime
        end function omp_get_wtime

        function omp_get_wtick() bind(c)
          double precision omp_get_wtick
        end function omp_get_wtick

        function omp_get_default_device() bind(c)
          import
          integer (kind=omp_integer_kind) omp_get_default_device
        end function omp_get_default_device

        subroutine omp_set_default_device(device_num) bind(c)
          import
          integer (kind=omp_integer_kind), value :: device_num
        end subroutine omp_set_default_device

        function omp_get_num_devices() bind(c)
          import
          integer (kind=omp_integer_kind) omp_get_num_devices
        end function omp_get_num_devices

        function omp_get_num_teams() bind(c)
          import
          integer (kind=omp_integer_kind) omp_get_num_teams
        end function omp_get_num_teams

        function omp_get_team_num() bind(c)
          import
          integer (kind=omp_integer_kind) omp_get_team_num
        end function omp_get_team_num

        function omp_is_initial_device() bind(c)
          import
          logical (kind=omp_logical_kind) omp_is_initial_device
        end function omp_is_initial_device

        function omp_get_initial_device() bind(c)
          import
          integer (kind=omp_integer_kind) omp_get_initial_device
        end function omp_get_initial_device

        function omp_get_device_num() bind(c)
          import
          integer (kind=omp_integer_kind) omp_get_device_num
        end function omp_get_device_num

        function omp_pause_resource(kind, device_num) bind(c)
          import
          integer (kind=omp_pause_resource_kind), value :: kind
          integer (kind=omp_integer_kind), value :: device_num
          integer (kind=omp_integer_kind) omp_pause_resource
        end function omp_pause_resource

        function omp_pause_resource_all(kind) bind(c)
          import
          integer (kind=omp_pause_resource_kind), value :: kind
          integer (kind=omp_integer_kind) omp_pause_resource_all
        end function omp_pause_resource_all

        function omp_get_supported_active_levels() bind(c)
          import
          integer(kind=omp_integer_kind)omp_get_supported_active_levels
        end function omp_get_supported_active_levels

        subroutine omp_fulfill_event(event) bind(c)
          import
          integer (kind=omp_event_handle_kind), value :: event
        end subroutine omp_fulfill_event

        subroutine omp_init_lock(svar) bind(c)
!DIR$ IF(__INTEL_COMPILER.GE.1400)
!DIR$ attributes known_intrinsic :: omp_init_lock
!DIR$ ENDIF
          import
          integer (kind=omp_lock_kind) svar
        end subroutine omp_init_lock

        subroutine omp_destroy_lock(svar) bind(c)
!DIR$ IF(__INTEL_COMPILER.GE.1400)
!DIR$ attributes known_intrinsic :: omp_destroy_lock
!DIR$ ENDIF
          import
          integer (kind=omp_lock_kind) svar
        end subroutine omp_destroy_lock

        subroutine omp_set_lock(svar) bind(c)
!DIR$ IF(__INTEL_COMPILER.GE.1400)
!DIR$ attributes known_intrinsic :: omp_set_lock
!DIR$ ENDIF
          import
          integer (kind=omp_lock_kind) svar
        end subroutine omp_set_lock

        subroutine omp_unset_lock(svar) bind(c)
!DIR$ IF(__INTEL_COMPILER.GE.1400)
!DIR$ attributes known_intrinsic :: omp_unset_lock
!DIR$ ENDIF
          import
          integer (kind=omp_lock_kind) svar
        end subroutine omp_unset_lock

        function omp_test_lock(svar) bind(c)
!DIR$ IF(__INTEL_COMPILER.GE.1400)
!DIR$ attributes known_intrinsic :: omp_test_lock
!DIR$ ENDIF
          import
          logical (kind=omp_logical_kind) omp_test_lock
          integer (kind=omp_lock_kind) svar
        end function omp_test_lock

        subroutine omp_init_nest_lock(nvar) bind(c)
!DIR$ IF(__INTEL_COMPILER.GE.1400)
!DIR$ attributes known_intrinsic :: omp_init_nest_lock
!DIR$ ENDIF
          import
          integer (kind=omp_nest_lock_kind) nvar
        end subroutine omp_init_nest_lock

        subroutine omp_destroy_nest_lock(nvar) bind(c)
!DIR$ IF(__INTEL_COMPILER.GE.1400)
!DIR$ attributes known_intrinsic :: omp_destroy_nest_lock
!DIR$ ENDIF
          import
          integer (kind=omp_nest_lock_kind) nvar
        end subroutine omp_destroy_nest_lock

        subroutine omp_set_nest_lock(nvar) bind(c)
!DIR$ IF(__INTEL_COMPILER.GE.1400)
!DIR$ attributes known_intrinsic :: omp_set_nest_lock
!DIR$ ENDIF
          import
          integer (kind=omp_nest_lock_kind) nvar
        end subroutine omp_set_nest_lock

        subroutine omp_unset_nest_lock(nvar) bind(c)
!DIR$ IF(__INTEL_COMPILER.GE.1400)
!DIR$ attributes known_intrinsic :: omp_unset_nest_lock
!DIR$ ENDIF
          import
          integer (kind=omp_nest_lock_kind) nvar
        end subroutine omp_unset_nest_lock

        function omp_test_nest_lock(nvar) bind(c)
!DIR$ IF(__INTEL_COMPILER.GE.1400)
!DIR$ attributes known_intrinsic :: omp_test_nest_lock
!DIR$ ENDIF
          import
          integer (kind=omp_integer_kind) omp_test_nest_lock
          integer (kind=omp_nest_lock_kind) nvar
        end function omp_test_nest_lock

        function omp_get_max_task_priority() bind(c)
          import
          integer (kind=omp_integer_kind) omp_get_max_task_priority
        end function omp_get_max_task_priority

        subroutine omp_init_lock_with_hint(svar, hint) bind(c)
          import
          integer (kind=omp_lock_kind) svar
          integer (kind=omp_lock_hint_kind), value :: hint
        end subroutine omp_init_lock_with_hint

        subroutine omp_init_nest_lock_with_hint(nvar, hint) bind(c)
          import
          integer (kind=omp_nest_lock_kind) nvar
          integer (kind=omp_lock_hint_kind), value :: hint
        end subroutine omp_init_nest_lock_with_hint

        function omp_control_tool(command, modifier, arg) bind(c)
          import
          integer (kind=omp_integer_kind) omp_control_tool
          integer (kind=omp_control_tool_kind), value :: command
          integer (kind=omp_control_tool_kind), value :: modifier
          integer (kind=kmp_pointer_kind), optional :: arg
        end function omp_control_tool

        function omp_init_allocator(memspace, ntraits, traits)
          import
          integer (omp_allocator_handle_kind) omp_init_allocator
          integer (omp_memspace_handle_kind) :: memspace
          integer (omp_integer_kind) :: ntraits
          type(omp_alloctrait), intent(in) :: traits(*)
        end function omp_init_allocator

        subroutine omp_destroy_allocator(allocator) bind(c)
          import
          integer (omp_allocator_handle_kind), value :: allocator
        end subroutine omp_destroy_allocator

        subroutine omp_set_default_allocator(allocator) bind(c)
          import
          integer (omp_allocator_handle_kind), value :: allocator
        end subroutine omp_set_default_allocator

        function omp_get_default_allocator() bind(c)
          import
          integer (omp_allocator_handle_kind) omp_get_default_allocator
        end function omp_get_default_allocator

        subroutine omp_set_affinity_format(format)
          character (len=*) :: format
        end subroutine omp_set_affinity_format

        function omp_get_affinity_format(buffer)
          import
          character (len=*) :: buffer
          integer (kind=kmp_size_t_kind) :: omp_get_affinity_format
        end function omp_get_affinity_format

        subroutine omp_display_affinity(format)
          character (len=*) :: format
        end subroutine omp_display_affinity

        function omp_capture_affinity(buffer, format)
          import
          character (len=*) :: format
          character (len=*) :: buffer
          integer (kind=kmp_size_t_kind) :: omp_capture_affinity
        end function omp_capture_affinity

        subroutine omp_set_num_teams(num_teams) bind(c)
          import
          integer (kind=omp_integer_kind), value :: num_teams
        end subroutine omp_set_num_teams

        function omp_get_max_teams() bind(c)
          import
          integer (kind=omp_integer_kind) omp_get_max_teams
        end function omp_get_max_teams

        subroutine omp_set_teams_thread_limit(thread_limit) bind(c)
          import
          integer (kind=omp_integer_kind), value :: thread_limit
        end subroutine omp_set_teams_thread_limit

        function omp_get_teams_thread_limit() bind(c)
          import
          integer (kind=omp_integer_kind) omp_get_teams_thread_limit
        end function omp_get_teams_thread_limit

        subroutine omp_display_env(verbose) bind(c)
          import
          logical (kind=omp_logical_kind), value :: verbose
        end subroutine omp_display_env

        function omp_target_alloc(size, device_num) bind(c)
          use, intrinsic :: iso_c_binding, only : c_ptr, c_size_t, c_int
          type(c_ptr) omp_target_alloc
          integer(c_size_t), value :: size
          integer(c_int), value :: device_num
        end function omp_target_alloc

        subroutine omp_target_free(device_ptr, device_num) bind(c)
          use, intrinsic :: iso_c_binding, only : c_ptr, c_int
          type(c_ptr), value :: device_ptr
          integer(c_int), value :: device_num
        end subroutine omp_target_free

        function omp_target_is_present(ptr, device_num) bind(c)
          use, intrinsic :: iso_c_binding, only : c_ptr, c_int
          integer(c_int) omp_target_is_present
          type(c_ptr), value :: ptr
          integer(c_int), value :: device_num
        end function omp_target_is_present

        function omp_target_memcpy(dst, src, length, dst_offset,                                                                    &
     &      src_offset, dst_device_num, src_device_num) bind(c)
          use, intrinsic :: iso_c_binding, only : c_ptr, c_int, c_size_t
          integer(c_int) omp_target_memcpy
          type(c_ptr), value :: dst, src
          integer(c_size_t), value :: length, dst_offset, src_offset
          integer(c_int), value :: dst_device_num, src_device_num
        end function omp_target_memcpy

        function omp_target_memcpy_rect(dst, src, element_size,                                                                     &
     &      num_dims, volume, dst_offsets, src_offsets, dst_dimensions,                                                             &
     &      src_dimensions, dst_device_num, src_device_num) bind(c)
          use, intrinsic :: iso_c_binding, only : c_ptr, c_int, c_size_t
          integer(c_int) omp_target_memcpy_rect
          type(c_ptr), value :: dst, src
          integer(c_size_t), value :: element_size
          integer(c_int), value :: num_dims, dst_device_num,                                                                        &
     &        src_device_num
          integer(c_size_t), intent(in) :: volume(*), dst_offsets(*),                                                               &
     &        src_offsets(*), dst_dimensions(*), src_dimensions(*)
        end function omp_target_memcpy_rect

        function omp_target_memcpy_async(dst, src, length, dst_offset,                                                              &
     &      src_offset, dst_device_num, src_device_num, depobj_count,                                                               &
     &      depobj_list) bind(c)
          use, intrinsic :: iso_c_binding, only : c_ptr, c_int, c_size_t
          import
          integer(c_int) omp_target_memcpy_async
          type(c_ptr), value :: dst, src
          integer(c_size_t), value :: length, dst_offset, src_offset
          integer(c_int), value :: dst_device_num, src_device_num,                                                                  &
     &        depobj_count
          integer(omp_depend_kind), optional :: depobj_list(*)
        end function omp_target_memcpy_async

        function omp_target_memcpy_rect_async(dst, src, element_size,                                                               &
     &      num_dims, volume, dst_offsets, src_offsets, dst_dimensions,                                                             &
     &      src_dimensions, dst_device_num, src_device_num,                                                                         &
     &      depobj_count, depobj_list) bind(c)
          use, intrinsic :: iso_c_binding, only : c_ptr, c_int, c_size_t
          import
          integer(c_int) omp_target_memcpy_rect_async
          type(c_ptr), value :: dst, src
          integer(c_size_t), value :: element_size
          integer(c_int), value :: num_dims, dst_device_num,                                                                        &
     &        src_device_num, depobj_count
          integer(c_size_t), intent(in) :: volume(*), dst_offsets(*),                                                               &
     &        src_offsets(*), dst_dimensions(*), src_dimensions(*)
          integer(omp_depend_kind), optional :: depobj_list(*)
        end function omp_target_memcpy_rect_async

        function omp_target_memset(ptr, val, count, device_num) bind(c)
          use, intrinsic :: iso_c_binding, only : c_ptr, c_int, c_size_t
          type(c_ptr) omp_target_memset
          type(c_ptr), value :: ptr
          integer(c_int), value :: val
          integer(c_size_t), value :: count
          integer(c_int), value :: device_num
        end function omp_target_memset

        function omp_target_memset_async(ptr, val, count, device_num,                                                               &
     &      depobj_count, depobj_list) bind(c)
          use, intrinsic :: iso_c_binding, only : c_ptr, c_int, c_size_t
          import
          type(c_ptr) omp_target_memset_async
          type(c_ptr), value :: ptr
          integer(c_int), value :: val
          integer(c_size_t), value :: count
          integer(c_int), value :: device_num
          integer(c_int), value :: depobj_count
          integer(omp_depend_kind), optional :: depobj_list(*)
        end function omp_target_memset_async

        function omp_target_associate_ptr(host_ptr, device_ptr, size,                                                               &
     &      device_offset, device_num) bind(c)
          use, intrinsic :: iso_c_binding, only : c_ptr, c_size_t, c_int
          integer(c_int) omp_target_associate_ptr
          type(c_ptr), value :: host_ptr, device_ptr
          integer(c_size_t), value :: size, device_offset
          integer(c_int), value :: device_num
        end function omp_target_associate_ptr

        function omp_get_mapped_ptr(ptr, device_num) bind(c)
          use, intrinsic :: iso_c_binding, only : c_ptr, c_int
          type(c_ptr) omp_get_mapped_ptr
          type(c_ptr), value :: ptr
          integer(c_int), value :: device_num
        end function omp_get_mapped_ptr

        function omp_target_disassociate_ptr(ptr, device_num) bind(c)
          use, intrinsic :: iso_c_binding, only : c_ptr, c_int
          integer(c_int) omp_target_disassociate_ptr
          type(c_ptr), value :: ptr
          integer(c_int), value :: device_num
        end function omp_target_disassociate_ptr

        function omp_target_is_accessible(ptr, size, device_num) bind(c)
          use, intrinsic :: iso_c_binding, only : c_ptr, c_size_t, c_int
          integer(c_int) omp_target_is_accessible
          type(c_ptr), value :: ptr
          integer(c_size_t), value :: size
          integer(c_int), value :: device_num
        end function omp_target_is_accessible

        function omp_alloc(size, allocator) bind(c)
          use, intrinsic :: iso_c_binding, only : c_ptr, c_size_t
          import :: omp_allocator_handle_kind
          type(c_ptr) omp_alloc
          integer(c_size_t), value :: size
          integer(omp_allocator_handle_kind), value :: allocator
        end function omp_alloc

        function omp_aligned_alloc(alignment, size, allocator) bind(c)
          use, intrinsic :: iso_c_binding, only : c_ptr, c_size_t
          import :: omp_allocator_handle_kind
          type(c_ptr) omp_aligned_alloc
          integer(c_size_t), value :: alignment, size
          integer(omp_allocator_handle_kind), value :: allocator
        end function omp_aligned_alloc

        function omp_calloc(nmemb, size, allocator) bind(c)
          use, intrinsic :: iso_c_binding, only : c_ptr, c_size_t
          import :: omp_allocator_handle_kind
          type(c_ptr) omp_calloc
          integer(c_size_t), value :: nmemb, size
          integer(omp_allocator_handle_kind), value :: allocator
        end function omp_calloc

        function omp_aligned_calloc(alignment, nmemb, size,                                                                         &
     &      allocator) bind(c)
          use, intrinsic :: iso_c_binding, only : c_ptr, c_size_t
          import :: omp_allocator_handle_kind
          type(c_ptr) omp_aligned_calloc
          integer(c_size_t), value :: alignment, nmemb, size
          integer(omp_allocator_handle_kind), value :: allocator
        end function omp_aligned_calloc

        function omp_realloc(ptr, size, allocator,                                                                                  &
     &      free_allocator) bind(c)
          use, intrinsic :: iso_c_binding, only : c_ptr, c_size_t
          import :: omp_allocator_handle_kind
          type(c_ptr) omp_realloc
          type(c_ptr), value :: ptr
          integer(c_size_t), value :: size
          integer(omp_allocator_handle_kind), value :: allocator
          integer(omp_allocator_handle_kind), value :: free_allocator
        end function omp_realloc

        subroutine omp_free(ptr, allocator) bind(c)
          use, intrinsic :: iso_c_binding, only : c_ptr
          import :: omp_allocator_handle_kind
          type(c_ptr), value :: ptr
          integer(omp_allocator_handle_kind), value :: allocator
        end subroutine omp_free

        function omp_in_explicit_task() bind(c)
          import
          logical (kind=omp_logical_kind) omp_in_explicit_task
        end function omp_in_explicit_task

        function omp_get_devices_memspace(ndevs, devs, memspace)
          import
          integer(omp_memspace_handle_kind) :: omp_get_devices_memspace
          integer, intent(in) :: ndevs
          integer, intent(in) :: devs(*)
          integer(omp_memspace_handle_kind), intent(in) :: memspace
        end function omp_get_devices_memspace

        function omp_get_device_memspace(dev, memspace)
          import
          integer(omp_memspace_handle_kind) :: omp_get_device_memspace
          integer, intent(in) :: dev
          integer(omp_memspace_handle_kind), intent(in) :: memspace
        end function omp_get_device_memspace

        function omp_get_devices_and_host_memspace(ndevs,devs,memspace)
          import
          integer(omp_memspace_handle_kind) ::                                                                                      &
     &        omp_get_devices_and_host_memspace
          integer, intent(in) :: ndevs
          integer, intent(in) :: devs(*)
          integer(omp_memspace_handle_kind), intent(in) :: memspace
        end function omp_get_devices_and_host_memspace

        function omp_get_device_and_host_memspace(dev, memspace)
          import
          integer(omp_memspace_handle_kind) ::                                                                                      &
     &        omp_get_device_and_host_memspace
          integer, intent(in) :: dev
          integer(omp_memspace_handle_kind), intent(in) :: memspace
        end function omp_get_device_and_host_memspace

        function omp_get_devices_all_memspace(memspace)
        import
        integer(omp_memspace_handle_kind)::omp_get_devices_all_memspace
        integer(omp_memspace_handle_kind), intent(in) :: memspace
        end function omp_get_devices_all_memspace

        function omp_get_devices_allocator(ndevs, devs, memspace)
          import
          integer(omp_allocator_handle_kind)::omp_get_devices_allocator
          integer, intent(in) :: ndevs
          integer, intent(in) :: devs(*)
          integer(omp_memspace_handle_kind), intent(in) :: memspace
        end function omp_get_devices_allocator

        function omp_get_device_allocator(dev, memspace)
          import
          integer(omp_allocator_handle_kind) :: omp_get_device_allocator
          integer, intent(in) :: dev
          integer(omp_memspace_handle_kind), intent(in) :: memspace
        end function omp_get_device_allocator

        function omp_get_devices_and_host_allocator(ndevs,devs,memspace)
          import
          integer(omp_allocator_handle_kind) ::                                                                                     &
     &        omp_get_devices_and_host_allocator
          integer, intent(in) :: ndevs
          integer, intent(in) :: devs(*)
          integer(omp_memspace_handle_kind), intent(in) :: memspace
        end function omp_get_devices_and_host_allocator

        function omp_get_device_and_host_allocator(dev, memspace)
          import
          integer(omp_allocator_handle_kind) ::                                                                                     &
     &        omp_get_device_and_host_allocator
          integer, intent(in) :: dev
          integer(omp_memspace_handle_kind), intent(in) :: memspace
        end function omp_get_device_and_host_allocator

        function omp_get_devices_all_allocator(memspace)
          import
          integer(omp_allocator_handle_kind) ::                                                                                     &
     &        omp_get_devices_all_allocator
          integer(omp_memspace_handle_kind), intent(in) :: memspace
        end function omp_get_devices_all_allocator

        function omp_get_memspace_num_resources(memspace)
          import
          integer omp_get_memspace_num_resources
          integer(omp_memspace_handle_kind), intent(in) :: memspace
        end function omp_get_memspace_num_resources

        function omp_get_submemspace(memspace, num_resources, resources)
          import
          integer(omp_memspace_handle_kind) omp_get_submemspace
          integer(omp_memspace_handle_kind), intent(in) :: memspace
          integer, intent(in) :: num_resources
          integer, intent(in) :: resources(*)
        end function omp_get_submemspace

        function omp_is_free_agent() bind(c)
          import
          integer (kind=omp_integer_kind) omp_is_free_agent
        end function omp_is_free_agent

        function omp_ancestor_is_free_agent(level) bind(c)
          import
          integer (kind=omp_integer_kind) omp_ancestor_is_free_agent
          integer (kind=omp_integer_kind), value :: level
        end function omp_ancestor_is_free_agent

!       ***
!       *** extensions
!       ***

        function omp_target_alloc_host(size, device_num) bind(c)
          use, intrinsic :: iso_c_binding, only : c_ptr
          import
          type(c_ptr) omp_target_alloc_host
          integer (kind=kmp_size_t_kind), value :: size
          integer (kind=omp_integer_kind), value :: device_num
        end function omp_target_alloc_host

        function omp_target_alloc_shared(size, device_num) bind(c)
          use, intrinsic :: iso_c_binding, only : c_ptr
          import
          type(c_ptr) omp_target_alloc_shared
          integer (kind=kmp_size_t_kind), value :: size
          integer (kind=omp_integer_kind), value :: device_num
        end function omp_target_alloc_shared

        function omp_target_alloc_device(size, device_num) bind(c)
          use, intrinsic :: iso_c_binding, only : c_ptr
          import
          type(c_ptr) omp_target_alloc_device
          integer (kind=kmp_size_t_kind), value :: size
          integer (kind=omp_integer_kind), value :: device_num
        end function omp_target_alloc_device

        function ompx_target_realloc(ptr, size, device) bind(c)
          use, intrinsic :: iso_c_binding, only : c_ptr, c_size_t, c_int
          type(c_ptr) ompx_target_realloc
          type(c_ptr), value :: ptr
          integer(c_size_t), value :: size
          integer(c_int), value :: device
        end function ompx_target_realloc

        function ompx_target_realloc_device(ptr, size, device) bind(c)
          use, intrinsic :: iso_c_binding, only : c_ptr, c_size_t, c_int
          type(c_ptr) ompx_target_realloc_device
          type(c_ptr), value :: ptr
          integer(c_size_t), value :: size
          integer(c_int), value :: device
        end function ompx_target_realloc_device

        function ompx_target_realloc_host(ptr, size, device) bind(c)
          use, intrinsic :: iso_c_binding, only : c_ptr, c_size_t, c_int
          type(c_ptr) ompx_target_realloc_host
          type(c_ptr), value :: ptr
          integer(c_size_t), value :: size
          integer(c_int), value :: device
        end function ompx_target_realloc_host

        function ompx_target_realloc_shared(ptr, size, device) bind(c)
          use, intrinsic :: iso_c_binding, only : c_ptr, c_size_t, c_int
          type(c_ptr) ompx_target_realloc_shared
          type(c_ptr), value :: ptr
          integer(c_size_t), value :: size
          integer(c_int), value :: device
        end function ompx_target_realloc_shared

        function ompx_target_aligned_alloc(aln, sz, dev) bind(c)
          use, intrinsic :: iso_c_binding, only : c_ptr, c_size_t, c_int
          type(c_ptr) ompx_target_aligned_alloc
          integer(c_size_t), value :: aln
          integer(c_size_t), value :: sz
          integer(c_int), value :: dev
        end function ompx_target_aligned_alloc

        function ompx_target_aligned_alloc_device(aln, sz, dev) bind(c)
          use, intrinsic :: iso_c_binding, only : c_ptr, c_size_t, c_int
          type(c_ptr) ompx_target_aligned_alloc_device
          integer(c_size_t), value :: aln
          integer(c_size_t), value :: sz
          integer(c_int), value :: dev
        end function ompx_target_aligned_alloc_device

        function ompx_target_aligned_alloc_host(aln, sz, dev) bind(c)
          use, intrinsic :: iso_c_binding, only : c_ptr, c_size_t, c_int
          type(c_ptr) ompx_target_aligned_alloc_host
          integer(c_size_t), value :: aln
          integer(c_size_t), value :: sz
          integer(c_int), value :: dev
        end function ompx_target_aligned_alloc_host

        function ompx_target_aligned_alloc_shared(aln, sz, dev) bind(c)
          use, intrinsic :: iso_c_binding, only : c_ptr, c_size_t, c_int
          type(c_ptr) ompx_target_aligned_alloc_shared
          integer(c_size_t), value :: aln
          integer(c_size_t), value :: sz
          integer(c_int), value :: dev
        end function ompx_target_aligned_alloc_shared

        function ompx_get_num_subdevices(device_num, level) bind(c)
          use, intrinsic :: iso_c_binding, only : c_int
          integer(c_int) ompx_get_num_subdevices
          integer(c_int), value :: device_num
          integer(c_int), value :: level
        end function ompx_get_num_subdevices

        function ompx_target_aligned_alloc_shared_with_hint(align, size,                                                            &
     &      hint, device) bind(c)
          use, intrinsic :: iso_c_binding, only : c_ptr, c_size_t
          import
          type(c_ptr) ompx_target_aligned_alloc_shared_with_hint
          integer(c_size_t), value :: align
          integer(c_size_t), value :: size
          integer(omp_integer_kind), value :: hint
          integer(omp_integer_kind), value :: device
        end function ompx_target_aligned_alloc_shared_with_hint

        function ompx_target_register_host_pointer(ptr, sz, dev) bind(c)
          use, intrinsic :: iso_c_binding, only : c_ptr, c_size_t
          import
          integer(omp_integer_kind) ompx_target_register_host_pointer
          type(c_ptr), value :: ptr
          integer(c_size_t), value :: sz
          integer(omp_integer_kind), value :: dev
        end function ompx_target_register_host_pointer

        subroutine ompx_target_unregister_host_pointer(ptr, dev) bind(c)
          use, intrinsic :: iso_c_binding, only : c_ptr
          import
          type(c_ptr), value :: ptr
          integer(omp_integer_kind), value :: dev
        end subroutine ompx_target_unregister_host_pointer

        function ompx_get_device_from_ptr(ptr) bind(c)
          use, intrinsic :: iso_c_binding, only : c_ptr
          import
          integer(omp_integer_kind) ompx_get_device_from_ptr
          type(c_ptr), value :: ptr
        end function ompx_get_device_from_ptr

        function ompx_get_dyn_cgroup_mem() bind(c)
          use, intrinsic :: iso_c_binding, only : c_ptr
          type(c_ptr) ompx_get_dyn_cgroup_mem
        end function ompx_get_dyn_cgroup_mem

!       ***
!       *** kmp_* entry points
!       ***

        subroutine kmp_set_stacksize(size) bind(c)
          import
          integer (kind=omp_integer_kind), value :: size
        end subroutine kmp_set_stacksize

        subroutine kmp_set_stacksize_s(size) bind(c)
          import
          integer (kind=kmp_size_t_kind), value :: size
        end subroutine kmp_set_stacksize_s

        subroutine kmp_set_blocktime(msec) bind(c)
          import
          integer (kind=omp_integer_kind), value :: msec
        end subroutine kmp_set_blocktime

        subroutine kmp_set_library_serial() bind(c)
        end subroutine kmp_set_library_serial

        subroutine kmp_set_library_turnaround() bind(c)
        end subroutine kmp_set_library_turnaround

        subroutine kmp_set_library_throughput() bind(c)
        end subroutine kmp_set_library_throughput

        subroutine kmp_set_library(libnum) bind(c)
          import
          integer (kind=omp_integer_kind), value :: libnum
        end subroutine kmp_set_library

        subroutine kmp_set_defaults(string)
          character (len=*) :: string
        end subroutine kmp_set_defaults

        function kmp_get_stacksize() bind(c)
          import
          integer (kind=omp_integer_kind) kmp_get_stacksize
        end function kmp_get_stacksize

        function kmp_get_stacksize_s() bind(c)
          import
          integer (kind=kmp_size_t_kind) kmp_get_stacksize_s
        end function kmp_get_stacksize_s

        function kmp_get_blocktime() bind(c)
          import
          integer (kind=omp_integer_kind) kmp_get_blocktime
        end function kmp_get_blocktime

        function kmp_get_library() bind(c)
          import
          integer (kind=omp_integer_kind) kmp_get_library
        end function kmp_get_library

        subroutine kmp_set_disp_num_buffers(num) bind(c)
          import
          integer (kind=omp_integer_kind), value :: num
        end subroutine kmp_set_disp_num_buffers

        function kmp_set_affinity(mask) bind(c)
          import
          integer (kind=omp_integer_kind) kmp_set_affinity
          integer (kind=kmp_affinity_mask_kind) mask
        end function kmp_set_affinity

        function kmp_get_affinity(mask) bind(c)
          import
          integer (kind=omp_integer_kind) kmp_get_affinity
          integer (kind=kmp_affinity_mask_kind) mask
        end function kmp_get_affinity

        function kmp_get_affinity_max_proc() bind(c)
          import
          integer (kind=omp_integer_kind) kmp_get_affinity_max_proc
        end function kmp_get_affinity_max_proc

        subroutine kmp_create_affinity_mask(mask) bind(c)
          import
          integer (kind=kmp_affinity_mask_kind) mask
        end subroutine kmp_create_affinity_mask

        subroutine kmp_destroy_affinity_mask(mask) bind(c)
          import
          integer (kind=kmp_affinity_mask_kind) mask
        end subroutine kmp_destroy_affinity_mask

        function kmp_set_affinity_mask_proc(proc, mask) bind(c)
          import
          integer (kind=omp_integer_kind) kmp_set_affinity_mask_proc
          integer (kind=omp_integer_kind), value :: proc
          integer (kind=kmp_affinity_mask_kind) mask
        end function kmp_set_affinity_mask_proc

        function kmp_unset_affinity_mask_proc(proc, mask) bind(c)
          import
          integer (kind=omp_integer_kind) kmp_unset_affinity_mask_proc
          integer (kind=omp_integer_kind), value :: proc
          integer (kind=kmp_affinity_mask_kind) mask
        end function kmp_unset_affinity_mask_proc

        function kmp_get_affinity_mask_proc(proc, mask) bind(c)
          import
          integer (kind=omp_integer_kind) kmp_get_affinity_mask_proc
          integer (kind=omp_integer_kind), value :: proc
          integer (kind=kmp_affinity_mask_kind) mask
        end function kmp_get_affinity_mask_proc

        function kmp_malloc(size) bind(c)
          import
          integer (kind=kmp_pointer_kind) kmp_malloc
          integer (kind=kmp_size_t_kind), value :: size
        end function kmp_malloc

        function kmp_aligned_malloc(size, alignment) bind(c)
          import
          integer (kind=kmp_pointer_kind) kmp_aligned_malloc
          integer (kind=kmp_size_t_kind), value :: size
          integer (kind=kmp_size_t_kind), value :: alignment
        end function kmp_aligned_malloc

        function kmp_calloc(nelem, elsize) bind(c)
          import
          integer (kind=kmp_pointer_kind) kmp_calloc
          integer (kind=kmp_size_t_kind), value :: nelem
          integer (kind=kmp_size_t_kind), value :: elsize
        end function kmp_calloc

        function kmp_realloc(ptr, size) bind(c)
          import
          integer (kind=kmp_pointer_kind) kmp_realloc
          integer (kind=kmp_pointer_kind), value :: ptr
          integer (kind=kmp_size_t_kind), value :: size
        end function kmp_realloc

        subroutine kmp_free(ptr) bind(c)
          import
          integer (kind=kmp_pointer_kind), value :: ptr
        end subroutine kmp_free

        subroutine kmp_set_warnings_on() bind(c)
        end subroutine kmp_set_warnings_on

        subroutine kmp_set_warnings_off() bind(c)
        end subroutine kmp_set_warnings_off

      end interface

!DIR$ IF DEFINED (__INTEL_OFFLOAD)

!DIR$ IF(__INTEL_COMPILER.LT.1900)
!DIR$ ATTRIBUTES OFFLOAD:MIC :: omp_set_num_threads
!DIR$ ATTRIBUTES OFFLOAD:MIC :: omp_set_dynamic
!DIR$ ATTRIBUTES OFFLOAD:MIC :: omp_set_nested
!DIR$ ATTRIBUTES OFFLOAD:MIC :: omp_get_num_threads
!DIR$ ATTRIBUTES OFFLOAD:MIC :: omp_get_max_threads
!DIR$ ATTRIBUTES OFFLOAD:MIC :: omp_get_thread_num
!DIR$ ATTRIBUTES OFFLOAD:MIC :: omp_get_num_procs
!DIR$ ATTRIBUTES OFFLOAD:MIC :: omp_in_parallel
!DIR$ ATTRIBUTES OFFLOAD:MIC :: omp_in_final
!DIR$ ATTRIBUTES OFFLOAD:MIC :: omp_get_dynamic
!DIR$ ATTRIBUTES OFFLOAD:MIC :: omp_get_nested
!DIR$ ATTRIBUTES OFFLOAD:MIC :: omp_get_thread_limit
!DIR$ ATTRIBUTES OFFLOAD:MIC :: omp_set_max_active_levels
!DIR$ ATTRIBUTES OFFLOAD:MIC :: omp_get_max_active_levels
!DIR$ ATTRIBUTES OFFLOAD:MIC :: omp_get_level
!DIR$ ATTRIBUTES OFFLOAD:MIC :: omp_get_active_level
!DIR$ ATTRIBUTES OFFLOAD:MIC :: omp_get_ancestor_thread_num
!DIR$ ATTRIBUTES OFFLOAD:MIC :: omp_get_team_size
!DIR$ ATTRIBUTES OFFLOAD:MIC :: omp_set_schedule
!DIR$ ATTRIBUTES OFFLOAD:MIC :: omp_get_schedule
!DIR$ ATTRIBUTES OFFLOAD:MIC :: omp_get_proc_bind
!DIR$ ATTRIBUTES OFFLOAD:MIC :: omp_get_wtime
!DIR$ ATTRIBUTES OFFLOAD:MIC :: omp_get_wtick
!DIR$ ATTRIBUTES OFFLOAD:MIC :: omp_get_default_device
!DIR$ ATTRIBUTES OFFLOAD:MIC :: omp_set_default_device
!DIR$ ATTRIBUTES OFFLOAD:MIC :: omp_is_initial_device
!DIR$ ATTRIBUTES OFFLOAD:MIC :: omp_get_initial_device
!DIR$ ATTRIBUTES OFFLOAD:MIC :: omp_get_num_devices
!DIR$ ATTRIBUTES OFFLOAD:MIC :: omp_get_device_num
!DIR$ ATTRIBUTES OFFLOAD:MIC :: omp_pause_resource
!DIR$ ATTRIBUTES OFFLOAD:MIC :: omp_pause_resource_all
!DIR$ ATTRIBUTES OFFLOAD:MIC :: omp_get_supported_active_levels
!DIR$ ATTRIBUTES OFFLOAD:MIC :: omp_fulfill_event
!DIR$ ATTRIBUTES OFFLOAD:MIC :: omp_get_num_teams
!DIR$ ATTRIBUTES OFFLOAD:MIC :: omp_get_team_num
!DIR$ ATTRIBUTES OFFLOAD:MIC :: omp_init_lock
!DIR$ ATTRIBUTES OFFLOAD:MIC :: omp_destroy_lock
!DIR$ ATTRIBUTES OFFLOAD:MIC :: omp_set_lock
!DIR$ ATTRIBUTES OFFLOAD:MIC :: omp_unset_lock
!DIR$ ATTRIBUTES OFFLOAD:MIC :: omp_test_lock
!DIR$ ATTRIBUTES OFFLOAD:MIC :: omp_init_nest_lock
!DIR$ ATTRIBUTES OFFLOAD:MIC :: omp_destroy_nest_lock
!DIR$ ATTRIBUTES OFFLOAD:MIC :: omp_set_nest_lock
!DIR$ ATTRIBUTES OFFLOAD:MIC :: omp_unset_nest_lock
!DIR$ ATTRIBUTES OFFLOAD:MIC :: omp_test_nest_lock
!DIR$ ATTRIBUTES OFFLOAD:MIC :: omp_get_max_task_priority
!DIR$ ATTRIBUTES OFFLOAD:MIC :: omp_set_affinity_format
!DIR$ ATTRIBUTES OFFLOAD:MIC :: omp_get_affinity_format
!DIR$ ATTRIBUTES OFFLOAD:MIC :: omp_display_affinity
!DIR$ ATTRIBUTES OFFLOAD:MIC :: omp_capture_affinity
!DIR$ ATTRIBUTES OFFLOAD:MIC :: kmp_set_stacksize
!DIR$ ATTRIBUTES OFFLOAD:MIC :: kmp_set_stacksize_s
!DIR$ ATTRIBUTES OFFLOAD:MIC :: kmp_set_blocktime
!DIR$ ATTRIBUTES OFFLOAD:MIC :: kmp_set_library_serial
!DIR$ ATTRIBUTES OFFLOAD:MIC :: kmp_set_library_turnaround
!DIR$ ATTRIBUTES OFFLOAD:MIC :: kmp_set_library_throughput
!DIR$ ATTRIBUTES OFFLOAD:MIC :: kmp_set_library
!DIR$ ATTRIBUTES OFFLOAD:MIC :: kmp_set_defaults
!DIR$ ATTRIBUTES OFFLOAD:MIC :: kmp_get_stacksize
!DIR$ ATTRIBUTES OFFLOAD:MIC :: kmp_get_stacksize_s
!DIR$ ATTRIBUTES OFFLOAD:MIC :: kmp_get_blocktime
!DIR$ ATTRIBUTES OFFLOAD:MIC :: kmp_get_library
!DIR$ ATTRIBUTES OFFLOAD:MIC :: kmp_set_disp_num_buffers
!DIR$ ATTRIBUTES OFFLOAD:MIC :: kmp_set_affinity
!DIR$ ATTRIBUTES OFFLOAD:MIC :: kmp_get_affinity
!DIR$ ATTRIBUTES OFFLOAD:MIC :: kmp_get_affinity_max_proc
!DIR$ ATTRIBUTES OFFLOAD:MIC :: kmp_create_affinity_mask
!DIR$ ATTRIBUTES OFFLOAD:MIC :: kmp_destroy_affinity_mask
!DIR$ ATTRIBUTES OFFLOAD:MIC :: kmp_set_affinity_mask_proc
!DIR$ ATTRIBUTES OFFLOAD:MIC :: kmp_unset_affinity_mask_proc
!DIR$ ATTRIBUTES OFFLOAD:MIC :: kmp_get_affinity_mask_proc
!DIR$ ATTRIBUTES OFFLOAD:MIC :: kmp_malloc
!DIR$ ATTRIBUTES OFFLOAD:MIC :: kmp_aligned_malloc
!DIR$ ATTRIBUTES OFFLOAD:MIC :: kmp_calloc
!DIR$ ATTRIBUTES OFFLOAD:MIC :: kmp_realloc
!DIR$ ATTRIBUTES OFFLOAD:MIC :: kmp_free
!DIR$ ATTRIBUTES OFFLOAD:MIC :: kmp_set_warnings_on
!DIR$ ATTRIBUTES OFFLOAD:MIC :: kmp_set_warnings_off
!DIR$ ATTRIBUTES OFFLOAD:MIC :: omp_init_lock_with_hint
!DIR$ ATTRIBUTES OFFLOAD:MIC :: omp_init_nest_lock_with_hint
!DIR$ ENDIF

!DIR$ IF(__INTEL_COMPILER.GE.1400)
!$omp declare target(omp_set_num_threads )
!$omp declare target(omp_set_dynamic )
!$omp declare target(omp_set_nested )
!$omp declare target(omp_get_num_threads )
!$omp declare target(omp_get_max_threads )
!$omp declare target(omp_get_thread_num )
!$omp declare target(omp_get_num_procs )
!$omp declare target(omp_in_parallel )
!$omp declare target(omp_in_final )
!$omp declare target(omp_get_dynamic )
!$omp declare target(omp_get_nested )
!$omp declare target(omp_get_thread_limit )
!$omp declare target(omp_set_max_active_levels )
!$omp declare target(omp_get_max_active_levels )
!$omp declare target(omp_get_level )
!$omp declare target(omp_get_active_level )
!$omp declare target(omp_get_ancestor_thread_num )
!$omp declare target(omp_get_team_size )
!$omp declare target(omp_set_schedule )
!$omp declare target(omp_get_schedule )
!$omp declare target(omp_get_proc_bind )
!$omp declare target(omp_get_wtime )
!$omp declare target(omp_get_wtick )
!$omp declare target(omp_get_default_device )
!$omp declare target(omp_set_default_device )
!$omp declare target(omp_is_initial_device )
!$omp declare target(omp_get_initial_device )
!$omp declare target(omp_get_num_devices )
!$omp declare target(omp_get_device_num )
!$omp declare target(omp_pause_resource )
!$omp declare target(omp_pause_resource_all )
!$omp declare target(omp_get_supported_active_levels )
!$omp declare target(omp_fulfill_event)
!$omp declare target(omp_get_num_teams )
!$omp declare target(omp_get_team_num )
!$omp declare target(omp_init_lock )
!$omp declare target(omp_destroy_lock )
!$omp declare target(omp_set_lock )
!$omp declare target(omp_unset_lock )
!$omp declare target(omp_test_lock )
!$omp declare target(omp_init_nest_lock )
!$omp declare target(omp_destroy_nest_lock )
!$omp declare target(omp_set_nest_lock )
!$omp declare target(omp_unset_nest_lock )
!$omp declare target(omp_test_nest_lock )
!$omp declare target(omp_get_max_task_priority )
!$omp declare target(omp_set_affinity_format )
!$omp declare target(omp_get_affinity_format )
!$omp declare target(omp_display_affinity )
!$omp declare target(omp_capture_affinity )
!$omp declare target(kmp_set_stacksize )
!$omp declare target(kmp_set_stacksize_s )
!$omp declare target(kmp_set_blocktime )
!$omp declare target(kmp_set_library_serial )
!$omp declare target(kmp_set_library_turnaround )
!$omp declare target(kmp_set_library_throughput )
!$omp declare target(kmp_set_library )
!$omp declare target(kmp_set_defaults )
!$omp declare target(kmp_get_stacksize )
!$omp declare target(kmp_get_stacksize_s )
!$omp declare target(kmp_get_blocktime )
!$omp declare target(kmp_get_library )
!$omp declare target(kmp_set_disp_num_buffers )
!$omp declare target(kmp_set_affinity )
!$omp declare target(kmp_get_affinity )
!$omp declare target(kmp_get_affinity_max_proc )
!$omp declare target(kmp_create_affinity_mask )
!$omp declare target(kmp_destroy_affinity_mask )
!$omp declare target(kmp_set_affinity_mask_proc )
!$omp declare target(kmp_unset_affinity_mask_proc )
!$omp declare target(kmp_get_affinity_mask_proc )
!$omp declare target(kmp_malloc )
!$omp declare target(kmp_aligned_malloc )
!$omp declare target(kmp_calloc )
!$omp declare target(kmp_realloc )
!$omp declare target(kmp_free )
!$omp declare target(kmp_set_warnings_on )
!$omp declare target(kmp_set_warnings_off )
!$omp declare target(omp_init_lock_with_hint )
!$omp declare target(omp_init_nest_lock_with_hint )
!DIR$ ENDIF
!DIR$ ENDIF
