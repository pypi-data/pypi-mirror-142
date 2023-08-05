// automatically generated by the FlatBuffers compiler, do not modify


#ifndef FLATBUFFERS_GENERATED_OPTIONALSCALARS_OPTIONAL_SCALARS_H_
#define FLATBUFFERS_GENERATED_OPTIONALSCALARS_OPTIONAL_SCALARS_H_

#include "flatbuffers/flatbuffers.h"

namespace optional_scalars {

struct ScalarStuff;
struct ScalarStuffBuilder;
struct ScalarStuffT;

inline const flatbuffers::TypeTable *ScalarStuffTypeTable();

enum class OptionalByte : int8_t {
  None = 0,
  One = 1,
  Two = 2,
  MIN = None,
  MAX = Two
};

inline const OptionalByte (&EnumValuesOptionalByte())[3] {
  static const OptionalByte values[] = {
    OptionalByte::None,
    OptionalByte::One,
    OptionalByte::Two
  };
  return values;
}

inline const char * const *EnumNamesOptionalByte() {
  static const char * const names[4] = {
    "None",
    "One",
    "Two",
    nullptr
  };
  return names;
}

inline const char *EnumNameOptionalByte(OptionalByte e) {
  if (flatbuffers::IsOutRange(e, OptionalByte::None, OptionalByte::Two)) return "";
  const size_t index = static_cast<size_t>(e);
  return EnumNamesOptionalByte()[index];
}

struct ScalarStuffT : public flatbuffers::NativeTable {
  typedef ScalarStuff TableType;
  int8_t just_i8 = 0;
  flatbuffers::Optional<int8_t> maybe_i8 = flatbuffers::nullopt;
  int8_t default_i8 = 42;
  uint8_t just_u8 = 0;
  flatbuffers::Optional<uint8_t> maybe_u8 = flatbuffers::nullopt;
  uint8_t default_u8 = 42;
  int16_t just_i16 = 0;
  flatbuffers::Optional<int16_t> maybe_i16 = flatbuffers::nullopt;
  int16_t default_i16 = 42;
  uint16_t just_u16 = 0;
  flatbuffers::Optional<uint16_t> maybe_u16 = flatbuffers::nullopt;
  uint16_t default_u16 = 42;
  int32_t just_i32 = 0;
  flatbuffers::Optional<int32_t> maybe_i32 = flatbuffers::nullopt;
  int32_t default_i32 = 42;
  uint32_t just_u32 = 0;
  flatbuffers::Optional<uint32_t> maybe_u32 = flatbuffers::nullopt;
  uint32_t default_u32 = 42;
  int64_t just_i64 = 0;
  flatbuffers::Optional<int64_t> maybe_i64 = flatbuffers::nullopt;
  int64_t default_i64 = 42LL;
  uint64_t just_u64 = 0;
  flatbuffers::Optional<uint64_t> maybe_u64 = flatbuffers::nullopt;
  uint64_t default_u64 = 42ULL;
  float just_f32 = 0.0f;
  flatbuffers::Optional<float> maybe_f32 = flatbuffers::nullopt;
  float default_f32 = 42.0f;
  double just_f64 = 0.0;
  flatbuffers::Optional<double> maybe_f64 = flatbuffers::nullopt;
  double default_f64 = 42.0;
  bool just_bool = false;
  flatbuffers::Optional<bool> maybe_bool = flatbuffers::nullopt;
  bool default_bool = true;
  optional_scalars::OptionalByte just_enum = optional_scalars::OptionalByte::None;
  flatbuffers::Optional<optional_scalars::OptionalByte> maybe_enum = flatbuffers::nullopt;
  optional_scalars::OptionalByte default_enum = optional_scalars::OptionalByte::One;
};

struct ScalarStuff FLATBUFFERS_FINAL_CLASS : private flatbuffers::Table {
  typedef ScalarStuffT NativeTableType;
  typedef ScalarStuffBuilder Builder;
  struct Traits;
  static const flatbuffers::TypeTable *MiniReflectTypeTable() {
    return ScalarStuffTypeTable();
  }
  enum FlatBuffersVTableOffset FLATBUFFERS_VTABLE_UNDERLYING_TYPE {
    VT_JUST_I8 = 4,
    VT_MAYBE_I8 = 6,
    VT_DEFAULT_I8 = 8,
    VT_JUST_U8 = 10,
    VT_MAYBE_U8 = 12,
    VT_DEFAULT_U8 = 14,
    VT_JUST_I16 = 16,
    VT_MAYBE_I16 = 18,
    VT_DEFAULT_I16 = 20,
    VT_JUST_U16 = 22,
    VT_MAYBE_U16 = 24,
    VT_DEFAULT_U16 = 26,
    VT_JUST_I32 = 28,
    VT_MAYBE_I32 = 30,
    VT_DEFAULT_I32 = 32,
    VT_JUST_U32 = 34,
    VT_MAYBE_U32 = 36,
    VT_DEFAULT_U32 = 38,
    VT_JUST_I64 = 40,
    VT_MAYBE_I64 = 42,
    VT_DEFAULT_I64 = 44,
    VT_JUST_U64 = 46,
    VT_MAYBE_U64 = 48,
    VT_DEFAULT_U64 = 50,
    VT_JUST_F32 = 52,
    VT_MAYBE_F32 = 54,
    VT_DEFAULT_F32 = 56,
    VT_JUST_F64 = 58,
    VT_MAYBE_F64 = 60,
    VT_DEFAULT_F64 = 62,
    VT_JUST_BOOL = 64,
    VT_MAYBE_BOOL = 66,
    VT_DEFAULT_BOOL = 68,
    VT_JUST_ENUM = 70,
    VT_MAYBE_ENUM = 72,
    VT_DEFAULT_ENUM = 74
  };
  int8_t just_i8() const {
    return GetField<int8_t>(VT_JUST_I8, 0);
  }
  bool mutate_just_i8(int8_t _just_i8) {
    return SetField<int8_t>(VT_JUST_I8, _just_i8, 0);
  }
  flatbuffers::Optional<int8_t> maybe_i8() const {
    return GetOptional<int8_t, int8_t>(VT_MAYBE_I8);
  }
  bool mutate_maybe_i8(int8_t _maybe_i8) {
    return SetField<int8_t>(VT_MAYBE_I8, _maybe_i8);
  }
  int8_t default_i8() const {
    return GetField<int8_t>(VT_DEFAULT_I8, 42);
  }
  bool mutate_default_i8(int8_t _default_i8) {
    return SetField<int8_t>(VT_DEFAULT_I8, _default_i8, 42);
  }
  uint8_t just_u8() const {
    return GetField<uint8_t>(VT_JUST_U8, 0);
  }
  bool mutate_just_u8(uint8_t _just_u8) {
    return SetField<uint8_t>(VT_JUST_U8, _just_u8, 0);
  }
  flatbuffers::Optional<uint8_t> maybe_u8() const {
    return GetOptional<uint8_t, uint8_t>(VT_MAYBE_U8);
  }
  bool mutate_maybe_u8(uint8_t _maybe_u8) {
    return SetField<uint8_t>(VT_MAYBE_U8, _maybe_u8);
  }
  uint8_t default_u8() const {
    return GetField<uint8_t>(VT_DEFAULT_U8, 42);
  }
  bool mutate_default_u8(uint8_t _default_u8) {
    return SetField<uint8_t>(VT_DEFAULT_U8, _default_u8, 42);
  }
  int16_t just_i16() const {
    return GetField<int16_t>(VT_JUST_I16, 0);
  }
  bool mutate_just_i16(int16_t _just_i16) {
    return SetField<int16_t>(VT_JUST_I16, _just_i16, 0);
  }
  flatbuffers::Optional<int16_t> maybe_i16() const {
    return GetOptional<int16_t, int16_t>(VT_MAYBE_I16);
  }
  bool mutate_maybe_i16(int16_t _maybe_i16) {
    return SetField<int16_t>(VT_MAYBE_I16, _maybe_i16);
  }
  int16_t default_i16() const {
    return GetField<int16_t>(VT_DEFAULT_I16, 42);
  }
  bool mutate_default_i16(int16_t _default_i16) {
    return SetField<int16_t>(VT_DEFAULT_I16, _default_i16, 42);
  }
  uint16_t just_u16() const {
    return GetField<uint16_t>(VT_JUST_U16, 0);
  }
  bool mutate_just_u16(uint16_t _just_u16) {
    return SetField<uint16_t>(VT_JUST_U16, _just_u16, 0);
  }
  flatbuffers::Optional<uint16_t> maybe_u16() const {
    return GetOptional<uint16_t, uint16_t>(VT_MAYBE_U16);
  }
  bool mutate_maybe_u16(uint16_t _maybe_u16) {
    return SetField<uint16_t>(VT_MAYBE_U16, _maybe_u16);
  }
  uint16_t default_u16() const {
    return GetField<uint16_t>(VT_DEFAULT_U16, 42);
  }
  bool mutate_default_u16(uint16_t _default_u16) {
    return SetField<uint16_t>(VT_DEFAULT_U16, _default_u16, 42);
  }
  int32_t just_i32() const {
    return GetField<int32_t>(VT_JUST_I32, 0);
  }
  bool mutate_just_i32(int32_t _just_i32) {
    return SetField<int32_t>(VT_JUST_I32, _just_i32, 0);
  }
  flatbuffers::Optional<int32_t> maybe_i32() const {
    return GetOptional<int32_t, int32_t>(VT_MAYBE_I32);
  }
  bool mutate_maybe_i32(int32_t _maybe_i32) {
    return SetField<int32_t>(VT_MAYBE_I32, _maybe_i32);
  }
  int32_t default_i32() const {
    return GetField<int32_t>(VT_DEFAULT_I32, 42);
  }
  bool mutate_default_i32(int32_t _default_i32) {
    return SetField<int32_t>(VT_DEFAULT_I32, _default_i32, 42);
  }
  uint32_t just_u32() const {
    return GetField<uint32_t>(VT_JUST_U32, 0);
  }
  bool mutate_just_u32(uint32_t _just_u32) {
    return SetField<uint32_t>(VT_JUST_U32, _just_u32, 0);
  }
  flatbuffers::Optional<uint32_t> maybe_u32() const {
    return GetOptional<uint32_t, uint32_t>(VT_MAYBE_U32);
  }
  bool mutate_maybe_u32(uint32_t _maybe_u32) {
    return SetField<uint32_t>(VT_MAYBE_U32, _maybe_u32);
  }
  uint32_t default_u32() const {
    return GetField<uint32_t>(VT_DEFAULT_U32, 42);
  }
  bool mutate_default_u32(uint32_t _default_u32) {
    return SetField<uint32_t>(VT_DEFAULT_U32, _default_u32, 42);
  }
  int64_t just_i64() const {
    return GetField<int64_t>(VT_JUST_I64, 0);
  }
  bool mutate_just_i64(int64_t _just_i64) {
    return SetField<int64_t>(VT_JUST_I64, _just_i64, 0);
  }
  flatbuffers::Optional<int64_t> maybe_i64() const {
    return GetOptional<int64_t, int64_t>(VT_MAYBE_I64);
  }
  bool mutate_maybe_i64(int64_t _maybe_i64) {
    return SetField<int64_t>(VT_MAYBE_I64, _maybe_i64);
  }
  int64_t default_i64() const {
    return GetField<int64_t>(VT_DEFAULT_I64, 42LL);
  }
  bool mutate_default_i64(int64_t _default_i64) {
    return SetField<int64_t>(VT_DEFAULT_I64, _default_i64, 42LL);
  }
  uint64_t just_u64() const {
    return GetField<uint64_t>(VT_JUST_U64, 0);
  }
  bool mutate_just_u64(uint64_t _just_u64) {
    return SetField<uint64_t>(VT_JUST_U64, _just_u64, 0);
  }
  flatbuffers::Optional<uint64_t> maybe_u64() const {
    return GetOptional<uint64_t, uint64_t>(VT_MAYBE_U64);
  }
  bool mutate_maybe_u64(uint64_t _maybe_u64) {
    return SetField<uint64_t>(VT_MAYBE_U64, _maybe_u64);
  }
  uint64_t default_u64() const {
    return GetField<uint64_t>(VT_DEFAULT_U64, 42ULL);
  }
  bool mutate_default_u64(uint64_t _default_u64) {
    return SetField<uint64_t>(VT_DEFAULT_U64, _default_u64, 42ULL);
  }
  float just_f32() const {
    return GetField<float>(VT_JUST_F32, 0.0f);
  }
  bool mutate_just_f32(float _just_f32) {
    return SetField<float>(VT_JUST_F32, _just_f32, 0.0f);
  }
  flatbuffers::Optional<float> maybe_f32() const {
    return GetOptional<float, float>(VT_MAYBE_F32);
  }
  bool mutate_maybe_f32(float _maybe_f32) {
    return SetField<float>(VT_MAYBE_F32, _maybe_f32);
  }
  float default_f32() const {
    return GetField<float>(VT_DEFAULT_F32, 42.0f);
  }
  bool mutate_default_f32(float _default_f32) {
    return SetField<float>(VT_DEFAULT_F32, _default_f32, 42.0f);
  }
  double just_f64() const {
    return GetField<double>(VT_JUST_F64, 0.0);
  }
  bool mutate_just_f64(double _just_f64) {
    return SetField<double>(VT_JUST_F64, _just_f64, 0.0);
  }
  flatbuffers::Optional<double> maybe_f64() const {
    return GetOptional<double, double>(VT_MAYBE_F64);
  }
  bool mutate_maybe_f64(double _maybe_f64) {
    return SetField<double>(VT_MAYBE_F64, _maybe_f64);
  }
  double default_f64() const {
    return GetField<double>(VT_DEFAULT_F64, 42.0);
  }
  bool mutate_default_f64(double _default_f64) {
    return SetField<double>(VT_DEFAULT_F64, _default_f64, 42.0);
  }
  bool just_bool() const {
    return GetField<uint8_t>(VT_JUST_BOOL, 0) != 0;
  }
  bool mutate_just_bool(bool _just_bool) {
    return SetField<uint8_t>(VT_JUST_BOOL, static_cast<uint8_t>(_just_bool), 0);
  }
  flatbuffers::Optional<bool> maybe_bool() const {
    return GetOptional<uint8_t, bool>(VT_MAYBE_BOOL);
  }
  bool mutate_maybe_bool(bool _maybe_bool) {
    return SetField<uint8_t>(VT_MAYBE_BOOL, static_cast<uint8_t>(_maybe_bool));
  }
  bool default_bool() const {
    return GetField<uint8_t>(VT_DEFAULT_BOOL, 1) != 0;
  }
  bool mutate_default_bool(bool _default_bool) {
    return SetField<uint8_t>(VT_DEFAULT_BOOL, static_cast<uint8_t>(_default_bool), 1);
  }
  optional_scalars::OptionalByte just_enum() const {
    return static_cast<optional_scalars::OptionalByte>(GetField<int8_t>(VT_JUST_ENUM, 0));
  }
  bool mutate_just_enum(optional_scalars::OptionalByte _just_enum) {
    return SetField<int8_t>(VT_JUST_ENUM, static_cast<int8_t>(_just_enum), 0);
  }
  flatbuffers::Optional<optional_scalars::OptionalByte> maybe_enum() const {
    return GetOptional<int8_t, optional_scalars::OptionalByte>(VT_MAYBE_ENUM);
  }
  bool mutate_maybe_enum(optional_scalars::OptionalByte _maybe_enum) {
    return SetField<int8_t>(VT_MAYBE_ENUM, static_cast<int8_t>(_maybe_enum));
  }
  optional_scalars::OptionalByte default_enum() const {
    return static_cast<optional_scalars::OptionalByte>(GetField<int8_t>(VT_DEFAULT_ENUM, 1));
  }
  bool mutate_default_enum(optional_scalars::OptionalByte _default_enum) {
    return SetField<int8_t>(VT_DEFAULT_ENUM, static_cast<int8_t>(_default_enum), 1);
  }
  template<size_t Index>
  auto get_field() const {
         if constexpr (Index == 0) return just_i8();
    else if constexpr (Index == 1) return maybe_i8();
    else if constexpr (Index == 2) return default_i8();
    else if constexpr (Index == 3) return just_u8();
    else if constexpr (Index == 4) return maybe_u8();
    else if constexpr (Index == 5) return default_u8();
    else if constexpr (Index == 6) return just_i16();
    else if constexpr (Index == 7) return maybe_i16();
    else if constexpr (Index == 8) return default_i16();
    else if constexpr (Index == 9) return just_u16();
    else if constexpr (Index == 10) return maybe_u16();
    else if constexpr (Index == 11) return default_u16();
    else if constexpr (Index == 12) return just_i32();
    else if constexpr (Index == 13) return maybe_i32();
    else if constexpr (Index == 14) return default_i32();
    else if constexpr (Index == 15) return just_u32();
    else if constexpr (Index == 16) return maybe_u32();
    else if constexpr (Index == 17) return default_u32();
    else if constexpr (Index == 18) return just_i64();
    else if constexpr (Index == 19) return maybe_i64();
    else if constexpr (Index == 20) return default_i64();
    else if constexpr (Index == 21) return just_u64();
    else if constexpr (Index == 22) return maybe_u64();
    else if constexpr (Index == 23) return default_u64();
    else if constexpr (Index == 24) return just_f32();
    else if constexpr (Index == 25) return maybe_f32();
    else if constexpr (Index == 26) return default_f32();
    else if constexpr (Index == 27) return just_f64();
    else if constexpr (Index == 28) return maybe_f64();
    else if constexpr (Index == 29) return default_f64();
    else if constexpr (Index == 30) return just_bool();
    else if constexpr (Index == 31) return maybe_bool();
    else if constexpr (Index == 32) return default_bool();
    else if constexpr (Index == 33) return just_enum();
    else if constexpr (Index == 34) return maybe_enum();
    else if constexpr (Index == 35) return default_enum();
    else static_assert(Index != Index, "Invalid Field Index");
  }
  bool Verify(flatbuffers::Verifier &verifier) const {
    return VerifyTableStart(verifier) &&
           VerifyField<int8_t>(verifier, VT_JUST_I8) &&
           VerifyField<int8_t>(verifier, VT_MAYBE_I8) &&
           VerifyField<int8_t>(verifier, VT_DEFAULT_I8) &&
           VerifyField<uint8_t>(verifier, VT_JUST_U8) &&
           VerifyField<uint8_t>(verifier, VT_MAYBE_U8) &&
           VerifyField<uint8_t>(verifier, VT_DEFAULT_U8) &&
           VerifyField<int16_t>(verifier, VT_JUST_I16) &&
           VerifyField<int16_t>(verifier, VT_MAYBE_I16) &&
           VerifyField<int16_t>(verifier, VT_DEFAULT_I16) &&
           VerifyField<uint16_t>(verifier, VT_JUST_U16) &&
           VerifyField<uint16_t>(verifier, VT_MAYBE_U16) &&
           VerifyField<uint16_t>(verifier, VT_DEFAULT_U16) &&
           VerifyField<int32_t>(verifier, VT_JUST_I32) &&
           VerifyField<int32_t>(verifier, VT_MAYBE_I32) &&
           VerifyField<int32_t>(verifier, VT_DEFAULT_I32) &&
           VerifyField<uint32_t>(verifier, VT_JUST_U32) &&
           VerifyField<uint32_t>(verifier, VT_MAYBE_U32) &&
           VerifyField<uint32_t>(verifier, VT_DEFAULT_U32) &&
           VerifyField<int64_t>(verifier, VT_JUST_I64) &&
           VerifyField<int64_t>(verifier, VT_MAYBE_I64) &&
           VerifyField<int64_t>(verifier, VT_DEFAULT_I64) &&
           VerifyField<uint64_t>(verifier, VT_JUST_U64) &&
           VerifyField<uint64_t>(verifier, VT_MAYBE_U64) &&
           VerifyField<uint64_t>(verifier, VT_DEFAULT_U64) &&
           VerifyField<float>(verifier, VT_JUST_F32) &&
           VerifyField<float>(verifier, VT_MAYBE_F32) &&
           VerifyField<float>(verifier, VT_DEFAULT_F32) &&
           VerifyField<double>(verifier, VT_JUST_F64) &&
           VerifyField<double>(verifier, VT_MAYBE_F64) &&
           VerifyField<double>(verifier, VT_DEFAULT_F64) &&
           VerifyField<uint8_t>(verifier, VT_JUST_BOOL) &&
           VerifyField<uint8_t>(verifier, VT_MAYBE_BOOL) &&
           VerifyField<uint8_t>(verifier, VT_DEFAULT_BOOL) &&
           VerifyField<int8_t>(verifier, VT_JUST_ENUM) &&
           VerifyField<int8_t>(verifier, VT_MAYBE_ENUM) &&
           VerifyField<int8_t>(verifier, VT_DEFAULT_ENUM) &&
           verifier.EndTable();
  }
  ScalarStuffT *UnPack(const flatbuffers::resolver_function_t *_resolver = nullptr) const;
  void UnPackTo(ScalarStuffT *_o, const flatbuffers::resolver_function_t *_resolver = nullptr) const;
  static flatbuffers::Offset<ScalarStuff> Pack(flatbuffers::FlatBufferBuilder &_fbb, const ScalarStuffT* _o, const flatbuffers::rehasher_function_t *_rehasher = nullptr);
};

struct ScalarStuffBuilder {
  typedef ScalarStuff Table;
  flatbuffers::FlatBufferBuilder &fbb_;
  flatbuffers::uoffset_t start_;
  void add_just_i8(int8_t just_i8) {
    fbb_.AddElement<int8_t>(ScalarStuff::VT_JUST_I8, just_i8, 0);
  }
  void add_maybe_i8(int8_t maybe_i8) {
    fbb_.AddElement<int8_t>(ScalarStuff::VT_MAYBE_I8, maybe_i8);
  }
  void add_default_i8(int8_t default_i8) {
    fbb_.AddElement<int8_t>(ScalarStuff::VT_DEFAULT_I8, default_i8, 42);
  }
  void add_just_u8(uint8_t just_u8) {
    fbb_.AddElement<uint8_t>(ScalarStuff::VT_JUST_U8, just_u8, 0);
  }
  void add_maybe_u8(uint8_t maybe_u8) {
    fbb_.AddElement<uint8_t>(ScalarStuff::VT_MAYBE_U8, maybe_u8);
  }
  void add_default_u8(uint8_t default_u8) {
    fbb_.AddElement<uint8_t>(ScalarStuff::VT_DEFAULT_U8, default_u8, 42);
  }
  void add_just_i16(int16_t just_i16) {
    fbb_.AddElement<int16_t>(ScalarStuff::VT_JUST_I16, just_i16, 0);
  }
  void add_maybe_i16(int16_t maybe_i16) {
    fbb_.AddElement<int16_t>(ScalarStuff::VT_MAYBE_I16, maybe_i16);
  }
  void add_default_i16(int16_t default_i16) {
    fbb_.AddElement<int16_t>(ScalarStuff::VT_DEFAULT_I16, default_i16, 42);
  }
  void add_just_u16(uint16_t just_u16) {
    fbb_.AddElement<uint16_t>(ScalarStuff::VT_JUST_U16, just_u16, 0);
  }
  void add_maybe_u16(uint16_t maybe_u16) {
    fbb_.AddElement<uint16_t>(ScalarStuff::VT_MAYBE_U16, maybe_u16);
  }
  void add_default_u16(uint16_t default_u16) {
    fbb_.AddElement<uint16_t>(ScalarStuff::VT_DEFAULT_U16, default_u16, 42);
  }
  void add_just_i32(int32_t just_i32) {
    fbb_.AddElement<int32_t>(ScalarStuff::VT_JUST_I32, just_i32, 0);
  }
  void add_maybe_i32(int32_t maybe_i32) {
    fbb_.AddElement<int32_t>(ScalarStuff::VT_MAYBE_I32, maybe_i32);
  }
  void add_default_i32(int32_t default_i32) {
    fbb_.AddElement<int32_t>(ScalarStuff::VT_DEFAULT_I32, default_i32, 42);
  }
  void add_just_u32(uint32_t just_u32) {
    fbb_.AddElement<uint32_t>(ScalarStuff::VT_JUST_U32, just_u32, 0);
  }
  void add_maybe_u32(uint32_t maybe_u32) {
    fbb_.AddElement<uint32_t>(ScalarStuff::VT_MAYBE_U32, maybe_u32);
  }
  void add_default_u32(uint32_t default_u32) {
    fbb_.AddElement<uint32_t>(ScalarStuff::VT_DEFAULT_U32, default_u32, 42);
  }
  void add_just_i64(int64_t just_i64) {
    fbb_.AddElement<int64_t>(ScalarStuff::VT_JUST_I64, just_i64, 0);
  }
  void add_maybe_i64(int64_t maybe_i64) {
    fbb_.AddElement<int64_t>(ScalarStuff::VT_MAYBE_I64, maybe_i64);
  }
  void add_default_i64(int64_t default_i64) {
    fbb_.AddElement<int64_t>(ScalarStuff::VT_DEFAULT_I64, default_i64, 42LL);
  }
  void add_just_u64(uint64_t just_u64) {
    fbb_.AddElement<uint64_t>(ScalarStuff::VT_JUST_U64, just_u64, 0);
  }
  void add_maybe_u64(uint64_t maybe_u64) {
    fbb_.AddElement<uint64_t>(ScalarStuff::VT_MAYBE_U64, maybe_u64);
  }
  void add_default_u64(uint64_t default_u64) {
    fbb_.AddElement<uint64_t>(ScalarStuff::VT_DEFAULT_U64, default_u64, 42ULL);
  }
  void add_just_f32(float just_f32) {
    fbb_.AddElement<float>(ScalarStuff::VT_JUST_F32, just_f32, 0.0f);
  }
  void add_maybe_f32(float maybe_f32) {
    fbb_.AddElement<float>(ScalarStuff::VT_MAYBE_F32, maybe_f32);
  }
  void add_default_f32(float default_f32) {
    fbb_.AddElement<float>(ScalarStuff::VT_DEFAULT_F32, default_f32, 42.0f);
  }
  void add_just_f64(double just_f64) {
    fbb_.AddElement<double>(ScalarStuff::VT_JUST_F64, just_f64, 0.0);
  }
  void add_maybe_f64(double maybe_f64) {
    fbb_.AddElement<double>(ScalarStuff::VT_MAYBE_F64, maybe_f64);
  }
  void add_default_f64(double default_f64) {
    fbb_.AddElement<double>(ScalarStuff::VT_DEFAULT_F64, default_f64, 42.0);
  }
  void add_just_bool(bool just_bool) {
    fbb_.AddElement<uint8_t>(ScalarStuff::VT_JUST_BOOL, static_cast<uint8_t>(just_bool), 0);
  }
  void add_maybe_bool(bool maybe_bool) {
    fbb_.AddElement<uint8_t>(ScalarStuff::VT_MAYBE_BOOL, static_cast<uint8_t>(maybe_bool));
  }
  void add_default_bool(bool default_bool) {
    fbb_.AddElement<uint8_t>(ScalarStuff::VT_DEFAULT_BOOL, static_cast<uint8_t>(default_bool), 1);
  }
  void add_just_enum(optional_scalars::OptionalByte just_enum) {
    fbb_.AddElement<int8_t>(ScalarStuff::VT_JUST_ENUM, static_cast<int8_t>(just_enum), 0);
  }
  void add_maybe_enum(optional_scalars::OptionalByte maybe_enum) {
    fbb_.AddElement<int8_t>(ScalarStuff::VT_MAYBE_ENUM, static_cast<int8_t>(maybe_enum));
  }
  void add_default_enum(optional_scalars::OptionalByte default_enum) {
    fbb_.AddElement<int8_t>(ScalarStuff::VT_DEFAULT_ENUM, static_cast<int8_t>(default_enum), 1);
  }
  explicit ScalarStuffBuilder(flatbuffers::FlatBufferBuilder &_fbb)
        : fbb_(_fbb) {
    start_ = fbb_.StartTable();
  }
  flatbuffers::Offset<ScalarStuff> Finish() {
    const auto end = fbb_.EndTable(start_);
    auto o = flatbuffers::Offset<ScalarStuff>(end);
    return o;
  }
};

inline flatbuffers::Offset<ScalarStuff> CreateScalarStuff(
    flatbuffers::FlatBufferBuilder &_fbb,
    int8_t just_i8 = 0,
    flatbuffers::Optional<int8_t> maybe_i8 = flatbuffers::nullopt,
    int8_t default_i8 = 42,
    uint8_t just_u8 = 0,
    flatbuffers::Optional<uint8_t> maybe_u8 = flatbuffers::nullopt,
    uint8_t default_u8 = 42,
    int16_t just_i16 = 0,
    flatbuffers::Optional<int16_t> maybe_i16 = flatbuffers::nullopt,
    int16_t default_i16 = 42,
    uint16_t just_u16 = 0,
    flatbuffers::Optional<uint16_t> maybe_u16 = flatbuffers::nullopt,
    uint16_t default_u16 = 42,
    int32_t just_i32 = 0,
    flatbuffers::Optional<int32_t> maybe_i32 = flatbuffers::nullopt,
    int32_t default_i32 = 42,
    uint32_t just_u32 = 0,
    flatbuffers::Optional<uint32_t> maybe_u32 = flatbuffers::nullopt,
    uint32_t default_u32 = 42,
    int64_t just_i64 = 0,
    flatbuffers::Optional<int64_t> maybe_i64 = flatbuffers::nullopt,
    int64_t default_i64 = 42LL,
    uint64_t just_u64 = 0,
    flatbuffers::Optional<uint64_t> maybe_u64 = flatbuffers::nullopt,
    uint64_t default_u64 = 42ULL,
    float just_f32 = 0.0f,
    flatbuffers::Optional<float> maybe_f32 = flatbuffers::nullopt,
    float default_f32 = 42.0f,
    double just_f64 = 0.0,
    flatbuffers::Optional<double> maybe_f64 = flatbuffers::nullopt,
    double default_f64 = 42.0,
    bool just_bool = false,
    flatbuffers::Optional<bool> maybe_bool = flatbuffers::nullopt,
    bool default_bool = true,
    optional_scalars::OptionalByte just_enum = optional_scalars::OptionalByte::None,
    flatbuffers::Optional<optional_scalars::OptionalByte> maybe_enum = flatbuffers::nullopt,
    optional_scalars::OptionalByte default_enum = optional_scalars::OptionalByte::One) {
  ScalarStuffBuilder builder_(_fbb);
  builder_.add_default_f64(default_f64);
  if(maybe_f64) { builder_.add_maybe_f64(*maybe_f64); }
  builder_.add_just_f64(just_f64);
  builder_.add_default_u64(default_u64);
  if(maybe_u64) { builder_.add_maybe_u64(*maybe_u64); }
  builder_.add_just_u64(just_u64);
  builder_.add_default_i64(default_i64);
  if(maybe_i64) { builder_.add_maybe_i64(*maybe_i64); }
  builder_.add_just_i64(just_i64);
  builder_.add_default_f32(default_f32);
  if(maybe_f32) { builder_.add_maybe_f32(*maybe_f32); }
  builder_.add_just_f32(just_f32);
  builder_.add_default_u32(default_u32);
  if(maybe_u32) { builder_.add_maybe_u32(*maybe_u32); }
  builder_.add_just_u32(just_u32);
  builder_.add_default_i32(default_i32);
  if(maybe_i32) { builder_.add_maybe_i32(*maybe_i32); }
  builder_.add_just_i32(just_i32);
  builder_.add_default_u16(default_u16);
  if(maybe_u16) { builder_.add_maybe_u16(*maybe_u16); }
  builder_.add_just_u16(just_u16);
  builder_.add_default_i16(default_i16);
  if(maybe_i16) { builder_.add_maybe_i16(*maybe_i16); }
  builder_.add_just_i16(just_i16);
  builder_.add_default_enum(default_enum);
  if(maybe_enum) { builder_.add_maybe_enum(*maybe_enum); }
  builder_.add_just_enum(just_enum);
  builder_.add_default_bool(default_bool);
  if(maybe_bool) { builder_.add_maybe_bool(*maybe_bool); }
  builder_.add_just_bool(just_bool);
  builder_.add_default_u8(default_u8);
  if(maybe_u8) { builder_.add_maybe_u8(*maybe_u8); }
  builder_.add_just_u8(just_u8);
  builder_.add_default_i8(default_i8);
  if(maybe_i8) { builder_.add_maybe_i8(*maybe_i8); }
  builder_.add_just_i8(just_i8);
  return builder_.Finish();
}

struct ScalarStuff::Traits {
  using type = ScalarStuff;
  static auto constexpr Create = CreateScalarStuff;
  static constexpr auto name = "ScalarStuff";
  static constexpr auto fully_qualified_name = "optional_scalars.ScalarStuff";
  static constexpr std::array<const char *, 36> field_names = {
    "just_i8",
    "maybe_i8",
    "default_i8",
    "just_u8",
    "maybe_u8",
    "default_u8",
    "just_i16",
    "maybe_i16",
    "default_i16",
    "just_u16",
    "maybe_u16",
    "default_u16",
    "just_i32",
    "maybe_i32",
    "default_i32",
    "just_u32",
    "maybe_u32",
    "default_u32",
    "just_i64",
    "maybe_i64",
    "default_i64",
    "just_u64",
    "maybe_u64",
    "default_u64",
    "just_f32",
    "maybe_f32",
    "default_f32",
    "just_f64",
    "maybe_f64",
    "default_f64",
    "just_bool",
    "maybe_bool",
    "default_bool",
    "just_enum",
    "maybe_enum",
    "default_enum"
  };
  template<size_t Index>
  using FieldType = decltype(std::declval<type>().get_field<Index>());
  static constexpr size_t fields_number = 36;
};

flatbuffers::Offset<ScalarStuff> CreateScalarStuff(flatbuffers::FlatBufferBuilder &_fbb, const ScalarStuffT *_o, const flatbuffers::rehasher_function_t *_rehasher = nullptr);

inline ScalarStuffT *ScalarStuff::UnPack(const flatbuffers::resolver_function_t *_resolver) const {
  auto _o = std::make_unique<ScalarStuffT>();
  UnPackTo(_o.get(), _resolver);
  return _o.release();
}

inline void ScalarStuff::UnPackTo(ScalarStuffT *_o, const flatbuffers::resolver_function_t *_resolver) const {
  (void)_o;
  (void)_resolver;
  { auto _e = just_i8(); _o->just_i8 = _e; }
  { auto _e = maybe_i8(); _o->maybe_i8 = _e; }
  { auto _e = default_i8(); _o->default_i8 = _e; }
  { auto _e = just_u8(); _o->just_u8 = _e; }
  { auto _e = maybe_u8(); _o->maybe_u8 = _e; }
  { auto _e = default_u8(); _o->default_u8 = _e; }
  { auto _e = just_i16(); _o->just_i16 = _e; }
  { auto _e = maybe_i16(); _o->maybe_i16 = _e; }
  { auto _e = default_i16(); _o->default_i16 = _e; }
  { auto _e = just_u16(); _o->just_u16 = _e; }
  { auto _e = maybe_u16(); _o->maybe_u16 = _e; }
  { auto _e = default_u16(); _o->default_u16 = _e; }
  { auto _e = just_i32(); _o->just_i32 = _e; }
  { auto _e = maybe_i32(); _o->maybe_i32 = _e; }
  { auto _e = default_i32(); _o->default_i32 = _e; }
  { auto _e = just_u32(); _o->just_u32 = _e; }
  { auto _e = maybe_u32(); _o->maybe_u32 = _e; }
  { auto _e = default_u32(); _o->default_u32 = _e; }
  { auto _e = just_i64(); _o->just_i64 = _e; }
  { auto _e = maybe_i64(); _o->maybe_i64 = _e; }
  { auto _e = default_i64(); _o->default_i64 = _e; }
  { auto _e = just_u64(); _o->just_u64 = _e; }
  { auto _e = maybe_u64(); _o->maybe_u64 = _e; }
  { auto _e = default_u64(); _o->default_u64 = _e; }
  { auto _e = just_f32(); _o->just_f32 = _e; }
  { auto _e = maybe_f32(); _o->maybe_f32 = _e; }
  { auto _e = default_f32(); _o->default_f32 = _e; }
  { auto _e = just_f64(); _o->just_f64 = _e; }
  { auto _e = maybe_f64(); _o->maybe_f64 = _e; }
  { auto _e = default_f64(); _o->default_f64 = _e; }
  { auto _e = just_bool(); _o->just_bool = _e; }
  { auto _e = maybe_bool(); _o->maybe_bool = _e; }
  { auto _e = default_bool(); _o->default_bool = _e; }
  { auto _e = just_enum(); _o->just_enum = _e; }
  { auto _e = maybe_enum(); _o->maybe_enum = _e; }
  { auto _e = default_enum(); _o->default_enum = _e; }
}

inline flatbuffers::Offset<ScalarStuff> ScalarStuff::Pack(flatbuffers::FlatBufferBuilder &_fbb, const ScalarStuffT* _o, const flatbuffers::rehasher_function_t *_rehasher) {
  return CreateScalarStuff(_fbb, _o, _rehasher);
}

inline flatbuffers::Offset<ScalarStuff> CreateScalarStuff(flatbuffers::FlatBufferBuilder &_fbb, const ScalarStuffT *_o, const flatbuffers::rehasher_function_t *_rehasher) {
  (void)_rehasher;
  (void)_o;
  struct _VectorArgs { flatbuffers::FlatBufferBuilder *__fbb; const ScalarStuffT* __o; const flatbuffers::rehasher_function_t *__rehasher; } _va = { &_fbb, _o, _rehasher}; (void)_va;
  auto _just_i8 = _o->just_i8;
  auto _maybe_i8 = _o->maybe_i8;
  auto _default_i8 = _o->default_i8;
  auto _just_u8 = _o->just_u8;
  auto _maybe_u8 = _o->maybe_u8;
  auto _default_u8 = _o->default_u8;
  auto _just_i16 = _o->just_i16;
  auto _maybe_i16 = _o->maybe_i16;
  auto _default_i16 = _o->default_i16;
  auto _just_u16 = _o->just_u16;
  auto _maybe_u16 = _o->maybe_u16;
  auto _default_u16 = _o->default_u16;
  auto _just_i32 = _o->just_i32;
  auto _maybe_i32 = _o->maybe_i32;
  auto _default_i32 = _o->default_i32;
  auto _just_u32 = _o->just_u32;
  auto _maybe_u32 = _o->maybe_u32;
  auto _default_u32 = _o->default_u32;
  auto _just_i64 = _o->just_i64;
  auto _maybe_i64 = _o->maybe_i64;
  auto _default_i64 = _o->default_i64;
  auto _just_u64 = _o->just_u64;
  auto _maybe_u64 = _o->maybe_u64;
  auto _default_u64 = _o->default_u64;
  auto _just_f32 = _o->just_f32;
  auto _maybe_f32 = _o->maybe_f32;
  auto _default_f32 = _o->default_f32;
  auto _just_f64 = _o->just_f64;
  auto _maybe_f64 = _o->maybe_f64;
  auto _default_f64 = _o->default_f64;
  auto _just_bool = _o->just_bool;
  auto _maybe_bool = _o->maybe_bool;
  auto _default_bool = _o->default_bool;
  auto _just_enum = _o->just_enum;
  auto _maybe_enum = _o->maybe_enum;
  auto _default_enum = _o->default_enum;
  return optional_scalars::CreateScalarStuff(
      _fbb,
      _just_i8,
      _maybe_i8,
      _default_i8,
      _just_u8,
      _maybe_u8,
      _default_u8,
      _just_i16,
      _maybe_i16,
      _default_i16,
      _just_u16,
      _maybe_u16,
      _default_u16,
      _just_i32,
      _maybe_i32,
      _default_i32,
      _just_u32,
      _maybe_u32,
      _default_u32,
      _just_i64,
      _maybe_i64,
      _default_i64,
      _just_u64,
      _maybe_u64,
      _default_u64,
      _just_f32,
      _maybe_f32,
      _default_f32,
      _just_f64,
      _maybe_f64,
      _default_f64,
      _just_bool,
      _maybe_bool,
      _default_bool,
      _just_enum,
      _maybe_enum,
      _default_enum);
}

inline const flatbuffers::TypeTable *OptionalByteTypeTable() {
  static const flatbuffers::TypeCode type_codes[] = {
    { flatbuffers::ET_CHAR, 0, 0 },
    { flatbuffers::ET_CHAR, 0, 0 },
    { flatbuffers::ET_CHAR, 0, 0 }
  };
  static const flatbuffers::TypeFunction type_refs[] = {
    optional_scalars::OptionalByteTypeTable
  };
  static const char * const names[] = {
    "None",
    "One",
    "Two"
  };
  static const flatbuffers::TypeTable tt = {
    flatbuffers::ST_ENUM, 3, type_codes, type_refs, nullptr, nullptr, names
  };
  return &tt;
}

inline const flatbuffers::TypeTable *ScalarStuffTypeTable() {
  static const flatbuffers::TypeCode type_codes[] = {
    { flatbuffers::ET_CHAR, 0, -1 },
    { flatbuffers::ET_CHAR, 0, -1 },
    { flatbuffers::ET_CHAR, 0, -1 },
    { flatbuffers::ET_UCHAR, 0, -1 },
    { flatbuffers::ET_UCHAR, 0, -1 },
    { flatbuffers::ET_UCHAR, 0, -1 },
    { flatbuffers::ET_SHORT, 0, -1 },
    { flatbuffers::ET_SHORT, 0, -1 },
    { flatbuffers::ET_SHORT, 0, -1 },
    { flatbuffers::ET_USHORT, 0, -1 },
    { flatbuffers::ET_USHORT, 0, -1 },
    { flatbuffers::ET_USHORT, 0, -1 },
    { flatbuffers::ET_INT, 0, -1 },
    { flatbuffers::ET_INT, 0, -1 },
    { flatbuffers::ET_INT, 0, -1 },
    { flatbuffers::ET_UINT, 0, -1 },
    { flatbuffers::ET_UINT, 0, -1 },
    { flatbuffers::ET_UINT, 0, -1 },
    { flatbuffers::ET_LONG, 0, -1 },
    { flatbuffers::ET_LONG, 0, -1 },
    { flatbuffers::ET_LONG, 0, -1 },
    { flatbuffers::ET_ULONG, 0, -1 },
    { flatbuffers::ET_ULONG, 0, -1 },
    { flatbuffers::ET_ULONG, 0, -1 },
    { flatbuffers::ET_FLOAT, 0, -1 },
    { flatbuffers::ET_FLOAT, 0, -1 },
    { flatbuffers::ET_FLOAT, 0, -1 },
    { flatbuffers::ET_DOUBLE, 0, -1 },
    { flatbuffers::ET_DOUBLE, 0, -1 },
    { flatbuffers::ET_DOUBLE, 0, -1 },
    { flatbuffers::ET_BOOL, 0, -1 },
    { flatbuffers::ET_BOOL, 0, -1 },
    { flatbuffers::ET_BOOL, 0, -1 },
    { flatbuffers::ET_CHAR, 0, 0 },
    { flatbuffers::ET_CHAR, 0, 0 },
    { flatbuffers::ET_CHAR, 0, 0 }
  };
  static const flatbuffers::TypeFunction type_refs[] = {
    optional_scalars::OptionalByteTypeTable
  };
  static const char * const names[] = {
    "just_i8",
    "maybe_i8",
    "default_i8",
    "just_u8",
    "maybe_u8",
    "default_u8",
    "just_i16",
    "maybe_i16",
    "default_i16",
    "just_u16",
    "maybe_u16",
    "default_u16",
    "just_i32",
    "maybe_i32",
    "default_i32",
    "just_u32",
    "maybe_u32",
    "default_u32",
    "just_i64",
    "maybe_i64",
    "default_i64",
    "just_u64",
    "maybe_u64",
    "default_u64",
    "just_f32",
    "maybe_f32",
    "default_f32",
    "just_f64",
    "maybe_f64",
    "default_f64",
    "just_bool",
    "maybe_bool",
    "default_bool",
    "just_enum",
    "maybe_enum",
    "default_enum"
  };
  static const flatbuffers::TypeTable tt = {
    flatbuffers::ST_TABLE, 36, type_codes, type_refs, nullptr, nullptr, names
  };
  return &tt;
}

inline const optional_scalars::ScalarStuff *GetScalarStuff(const void *buf) {
  return flatbuffers::GetRoot<optional_scalars::ScalarStuff>(buf);
}

inline const optional_scalars::ScalarStuff *GetSizePrefixedScalarStuff(const void *buf) {
  return flatbuffers::GetSizePrefixedRoot<optional_scalars::ScalarStuff>(buf);
}

inline ScalarStuff *GetMutableScalarStuff(void *buf) {
  return flatbuffers::GetMutableRoot<ScalarStuff>(buf);
}

inline const char *ScalarStuffIdentifier() {
  return "NULL";
}

inline bool ScalarStuffBufferHasIdentifier(const void *buf) {
  return flatbuffers::BufferHasIdentifier(
      buf, ScalarStuffIdentifier());
}

inline bool VerifyScalarStuffBuffer(
    flatbuffers::Verifier &verifier) {
  return verifier.VerifyBuffer<optional_scalars::ScalarStuff>(ScalarStuffIdentifier());
}

inline bool VerifySizePrefixedScalarStuffBuffer(
    flatbuffers::Verifier &verifier) {
  return verifier.VerifySizePrefixedBuffer<optional_scalars::ScalarStuff>(ScalarStuffIdentifier());
}

inline const char *ScalarStuffExtension() {
  return "mon";
}

inline void FinishScalarStuffBuffer(
    flatbuffers::FlatBufferBuilder &fbb,
    flatbuffers::Offset<optional_scalars::ScalarStuff> root) {
  fbb.Finish(root, ScalarStuffIdentifier());
}

inline void FinishSizePrefixedScalarStuffBuffer(
    flatbuffers::FlatBufferBuilder &fbb,
    flatbuffers::Offset<optional_scalars::ScalarStuff> root) {
  fbb.FinishSizePrefixed(root, ScalarStuffIdentifier());
}

inline std::unique_ptr<optional_scalars::ScalarStuffT> UnPackScalarStuff(
    const void *buf,
    const flatbuffers::resolver_function_t *res = nullptr) {
  return std::unique_ptr<optional_scalars::ScalarStuffT>(GetScalarStuff(buf)->UnPack(res));
}

inline std::unique_ptr<optional_scalars::ScalarStuffT> UnPackSizePrefixedScalarStuff(
    const void *buf,
    const flatbuffers::resolver_function_t *res = nullptr) {
  return std::unique_ptr<optional_scalars::ScalarStuffT>(GetSizePrefixedScalarStuff(buf)->UnPack(res));
}

}  // namespace optional_scalars

#endif  // FLATBUFFERS_GENERATED_OPTIONALSCALARS_OPTIONAL_SCALARS_H_
