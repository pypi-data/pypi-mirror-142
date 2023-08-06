
#ifndef __ENCODERCOMPRESSIONMULTITONE__
#define __ENCODERCOMPRESSIONMULTITONE__

#include "Encoder.h"

namespace SPEECHY
{
  class EncoderCompressionMultiTone : public Encoder
  {
  public:
    EncoderCompressionMultiTone(float samplingRate, int buffsize, int windowSize);
    ~EncoderCompressionMultiTone(void);

    float* mCurrentFreqs;
    float* mCurrentFreqsLoudness;

    int EncodeDataToAudioBuffer(const char *stringToEncode, int type, int size, const char *melodyString, int melodySize);
    int GetEncodedAudioBuffer(float *audioBuffer);
    int ResetEncodedAudioBuffer();
  };
}

#endif //__ENCODERCOMPRESSIONMULTITONE__