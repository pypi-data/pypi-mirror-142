/*--------------------------------------------------------------------------------
 OxySoundCoreLib_api.h
 
 CONFIDENTIAL: This document contains confidential information. 
 Do not disclose any information contained in this document to any
 third-party without the prior written consent of OxyCom, Ltd.
 --------------------------------------------------------------------------------*/

// This file contains all the prototypes needed for
// transmitting numeric data through sound 


#ifndef __SPEECHYCORELIB_API__
#define __SPEECHYCORELIB_API__

#ifndef __APPLE__
  #ifdef SPEECHY_AS_DLL
    #define SPEECHY_DLLEXPORT __declspec(dllexport)
  #else
    #define SPEECHY_DLLEXPORT
  #endif

#else
  #define SPEECHY_DLLEXPORT __attribute__((visibility("default")))
#endif

#include "stdint.h"

#ifdef __cplusplus
extern "C" {
#endif //__cplusplus

  enum SPEECHY_MODE { SPEECHY_MODE_AUDIBLE=2, SPEECHY_MODE_NONAUDIBLE=3, SPEECHY_MODE_COMPRESSION=4, SPEECHY_MODE_ALL=5, SPEECHY_MODE_CUSTOM=6 };
  SPEECHY_DLLEXPORT void *SPEECHY_Create();
  SPEECHY_DLLEXPORT void SPEECHY_Destroy(void *oxyingObject);

  ///////////////////////////////////////////
  ///// VERSIONING
  ///////////////////////////////////////////
  //Return string with version information
  SPEECHY_DLLEXPORT const char* SPEECHY_GetVersion();

  //Return string with version information
  SPEECHY_DLLEXPORT int32_t SPEECHY_GetVersionInfo(char * versioninfo);

  ///////////////////////////////////////////
  ///// CONFIGURE
  ///////////////////////////////////////////

  //SPEECHY_Configure function, call this function to configure parameters of the OxyComCore Library
  //* Parameters:
  //    mode: mode (2 for audible, 3 for non-audible)
  //    samplingRate: sampling rate in Hz
  //    nChannels: number of channels of the input audio
  //    oxyingObject: SPEECHY object instance, created in SPEECHY_Create()
  //* Returns: 0=ok, <0=fail
  SPEECHY_DLLEXPORT int32_t SPEECHY_Configure(int mode, float samplingRate, int32_t bufferSize, void *oxyingObject);
 
  //SPEECHY_SetAudioSignature function, call this function to set a personalized audio that will be played 
  // simultaneously during oxying playback on top of non-audible, audible or hidden oxys
  //* Parameters:
  //    samplesSize: number of samples in samples buffer (maximum size is 2 seconds= 44100*2)
  //    samples: array with samples (44Khz, 16bits, mono)
  //    oxyingObject: SPEECHY object instance, created in SPEECHY_Create()
  //* Returns: 0=ok, <0=fail

  SPEECHY_DLLEXPORT int32_t SPEECHY_SetAudioSignature(int32_t samplesSize, const float *samplesBuffer, void *oxyingObject);
 
  //SPEECHY_EncodeDataToAudioBuffer function
  //* Parameters:
  //    stringToEncode: string containing the characters to encode
  //    size: number of characters in string characters to encode
  //    type: 0 for encoding only tones, 1 for encoding tones + R2D2 sounds, 2 for encoding melody
  //    melodyString: string containing characters to synthesize melody over the tones (null if type parameter is 0 or 1)
  //    melodySize: size of melody in number of notes (0 if type parameter is 0 or 1)
  //    oxyingObject: SPEECHY object instance, created in SPEECHY_Create()
  //* Returns: number of samples in encoded audio buffer

  SPEECHY_DLLEXPORT int32_t SPEECHY_EncodeDataToAudioBuffer(const char *stringToEncode, int32_t size, int32_t type, const char *melodyString, int32_t melodySize, void *oxyingObject);
 
  //SPEECHY_GetEncodedAudioBuffer function
  //* Parameters:
  //    audioBuffer: float array of bufferSize size to fill with encoded audio data
  //    oxyingObject: SPEECHY object instance, created in SPEECHY_Create()  
  //* Returns: number of samples read, maximum will be configured bufferSize, 0 or < bufferSize means that end has been reached
  SPEECHY_DLLEXPORT int32_t SPEECHY_GetEncodedAudioBuffer(float *audioBuffer, void *oxyingObject);

  //SPEECHY_CreateAudioBufferFromData function, resets the read index on the internal buffer that has the encoded string
  //* Parameters:
  //    oxyingObject: SPEECHY object instance, created in SPEECHY_Create()  
  //* Returns: 0=ok, <0=fail
  SPEECHY_DLLEXPORT int32_t SPEECHY_ResetEncodedAudioBuffer(void *oxyingObject);


  //SPEECHY_DecodeAudioBuffer function, receives an audiobuffer of specified size and outputs if encoded data is found
  //* Parameters:
  //    audioBuffer: float array of bufferSize size with audio data to be decoded
  //    size: size of audioBuffer
  //    oxyingObject: SPEECHY object instance, created in SPEECHY_Create()  
  //* Returns: -1 if no decoded data is found, -2 if start token is found, -3 if complete word has been decoded, positive number if character is decoded (number is the token idx)

  SPEECHY_DLLEXPORT int32_t SPEECHY_DecodeAudioBuffer(float *audioBuffer, int size, void *oxyingObject);

  //SPEECHY_GetDecodedData function, retrieves the last decoded data found
  //* Parameters:
  //    stringDecoded: string containing decoded characters
  //    oxyingObject: SPEECHY object instance, created in SPEECHY_Create()
  //* Returns: 0 if no decoded data is available, >0 if data is available and it's ok, <0 if data is available but it's wrong, for the last two cases the return value magnitude contains number of characters in string decoded
  SPEECHY_DLLEXPORT int32_t SPEECHY_GetDecodedData(char *stringDecoded, void *oxyingObject);
  //we should include maxsize?? int32_t maxsize

  //SPEECHY_GetConfidence function, outputs Reception Quality Measure to give confidence about the received audio. 
  // A Reception Quality value of 1.0 will mean that the reception conditions are ideal, a lower value will mean that 
  // listener is in a noisy environment, the listener should be closer to the transmitter, etc.
  //* Parameters:
  //    oxyingObject: SPEECHY object instance, created in SPEECHY_Create()
  //* Returns: confidence value from 0.0 o 1.0
  SPEECHY_DLLEXPORT float SPEECHY_GetConfidence(void *oxyingObject); //Get global confidence (combination of the other confidence values)
  SPEECHY_DLLEXPORT float SPEECHY_GetConfidenceError(void *oxyingObject); //Get confidence due to tokens corrected by correction algorithm
  SPEECHY_DLLEXPORT float SPEECHY_GetConfidenceNoise(void *oxyingObject); //Get confidence due to signal to noise ratio in received audio

  SPEECHY_DLLEXPORT float SPEECHY_GetReceivedOxysVolume(void *oxyingObject); // Get average received volume of last audio transmission in DB

  //SPEECHY_GetDecodedMode function, outputs an integer representation of the decoded mode found from all 
  // available decoding modes, it only makes sense when decoder is configured with the ALL mode, for other modes
  // decoded mode will be always the same as the decoding mode.
  //* Parameters:
  //    none
  //* Returns: decoded mode found ( AUDIBLE = 0, NONAUDIBLE = 1, COMPRESSION = 2 )
  SPEECHY_DLLEXPORT int32_t SPEECHY_GetDecodedMode(void *oxyingObject);

  /////////////////////////////////////////////////////////////////////////////
  // FOR CUSTOM MODE
  //////////////////////////////////////////////////////////

  SPEECHY_DLLEXPORT int32_t SPEECHY_SetCustomBaseFreq(float baseFreq, int oxysSeparation, void *oxyingObject);

  /////////////////////////////////////////////////////////////////////////////
  // Functions to get decoding frequency range (begin range frequency and end range frequency)
  SPEECHY_DLLEXPORT float SPEECHY_GetDecodingBeginFreq(void *oxyingObject);
  SPEECHY_DLLEXPORT float SPEECHY_GetDecodingEndFreq(void *oxyingObject);

  /////////////////////////////////////////////////////////////////////////////
  // FOR SYNTH MODE //////////////////////////////////////////////////////////

  SPEECHY_DLLEXPORT int32_t SPEECHY_SetSynthMode(int synthMode, void *oxyingObject);
  SPEECHY_DLLEXPORT int32_t SPEECHY_SetSynthVolume(float synthVolume, void *oxyingObject);


  //Not used
  SPEECHY_DLLEXPORT int32_t SPEECHY_GetSpectrum(float *spectrumBuffer, void *oxyingObject);
  

#ifdef __cplusplus
}
#endif //__cplusplus

#endif //__SPEECHYCORELIB_API__
