// automatically generated by the FlatBuffers compiler, do not modify


#ifndef FLATBUFFERS_GENERATED_ANIMAL_COM_FBS_APP_H_
#define FLATBUFFERS_GENERATED_ANIMAL_COM_FBS_APP_H_

#include "flatbuffers/flatbuffers.h"

namespace com {
namespace fbs {
namespace app {

struct Animal;
struct AnimalBuilder;

struct Animal FLATBUFFERS_FINAL_CLASS : private flatbuffers::Table {
  typedef AnimalBuilder Builder;
  enum FlatBuffersVTableOffset FLATBUFFERS_VTABLE_UNDERLYING_TYPE {
    VT_NAME = 4,
    VT_SOUND = 6,
    VT_WEIGHT = 8
  };
  const flatbuffers::String *name() const {
    return GetPointer<const flatbuffers::String *>(VT_NAME);
  }
  const flatbuffers::String *sound() const {
    return GetPointer<const flatbuffers::String *>(VT_SOUND);
  }
  uint16_t weight() const {
    return GetField<uint16_t>(VT_WEIGHT, 0);
  }
  bool Verify(flatbuffers::Verifier &verifier) const {
    return VerifyTableStart(verifier) &&
           VerifyOffset(verifier, VT_NAME) &&
           verifier.VerifyString(name()) &&
           VerifyOffset(verifier, VT_SOUND) &&
           verifier.VerifyString(sound()) &&
           VerifyField<uint16_t>(verifier, VT_WEIGHT) &&
           verifier.EndTable();
  }
};

struct AnimalBuilder {
  typedef Animal Table;
  flatbuffers::FlatBufferBuilder &fbb_;
  flatbuffers::uoffset_t start_;
  void add_name(flatbuffers::Offset<flatbuffers::String> name) {
    fbb_.AddOffset(Animal::VT_NAME, name);
  }
  void add_sound(flatbuffers::Offset<flatbuffers::String> sound) {
    fbb_.AddOffset(Animal::VT_SOUND, sound);
  }
  void add_weight(uint16_t weight) {
    fbb_.AddElement<uint16_t>(Animal::VT_WEIGHT, weight, 0);
  }
  explicit AnimalBuilder(flatbuffers::FlatBufferBuilder &_fbb)
        : fbb_(_fbb) {
    start_ = fbb_.StartTable();
  }
  AnimalBuilder &operator=(const AnimalBuilder &);
  flatbuffers::Offset<Animal> Finish() {
    const auto end = fbb_.EndTable(start_);
    auto o = flatbuffers::Offset<Animal>(end);
    return o;
  }
};

inline flatbuffers::Offset<Animal> CreateAnimal(
    flatbuffers::FlatBufferBuilder &_fbb,
    flatbuffers::Offset<flatbuffers::String> name = 0,
    flatbuffers::Offset<flatbuffers::String> sound = 0,
    uint16_t weight = 0) {
  AnimalBuilder builder_(_fbb);
  builder_.add_sound(sound);
  builder_.add_name(name);
  builder_.add_weight(weight);
  return builder_.Finish();
}

inline flatbuffers::Offset<Animal> CreateAnimalDirect(
    flatbuffers::FlatBufferBuilder &_fbb,
    const char *name = nullptr,
    const char *sound = nullptr,
    uint16_t weight = 0) {
  auto name__ = name ? _fbb.CreateString(name) : 0;
  auto sound__ = sound ? _fbb.CreateString(sound) : 0;
  return com::fbs::app::CreateAnimal(
      _fbb,
      name__,
      sound__,
      weight);
}

inline const com::fbs::app::Animal *GetAnimal(const void *buf) {
  return flatbuffers::GetRoot<com::fbs::app::Animal>(buf);
}

inline const com::fbs::app::Animal *GetSizePrefixedAnimal(const void *buf) {
  return flatbuffers::GetSizePrefixedRoot<com::fbs::app::Animal>(buf);
}

inline bool VerifyAnimalBuffer(
    flatbuffers::Verifier &verifier) {
  return verifier.VerifyBuffer<com::fbs::app::Animal>(nullptr);
}

inline bool VerifySizePrefixedAnimalBuffer(
    flatbuffers::Verifier &verifier) {
  return verifier.VerifySizePrefixedBuffer<com::fbs::app::Animal>(nullptr);
}

inline void FinishAnimalBuffer(
    flatbuffers::FlatBufferBuilder &fbb,
    flatbuffers::Offset<com::fbs::app::Animal> root) {
  fbb.Finish(root);
}

inline void FinishSizePrefixedAnimalBuffer(
    flatbuffers::FlatBufferBuilder &fbb,
    flatbuffers::Offset<com::fbs::app::Animal> root) {
  fbb.FinishSizePrefixed(root);
}

}  // namespace app
}  // namespace fbs
}  // namespace com

#endif  // FLATBUFFERS_GENERATED_ANIMAL_COM_FBS_APP_H_
