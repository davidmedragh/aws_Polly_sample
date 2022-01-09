# aws_Polly_sample

## Amazon Polly:

https://docs.aws.amazon.com/polly/latest/dg/what-is.html

```aws polly describe-voices --language en-US --output table```

![poly](./img/polly.JPG)

API Requests
Examine the request that is being transmitted in step 2 of Figure 1.3. When the SDK makes the request to Amazon Polly, it submits a JSON body using a standard HTTP POST to https://polly.us-west-2.amazonaws.com/v1/speech.

The SDK sets the following properties in the request:


P/usr/bin/python3 /home/dmedragh/github_davidmedragh/aws_Polly_sample/polly.py
2022-01-07 23:41:24,255 botocore.hooks [DEBUG] Changing event name from creating-client-class.iot-data to creating-client-class.iot-data-plane
2022-01-07 23:41:24,256 botocore.hooks [DEBUG] Changing event name from before-call.apigateway to before-call.api-gateway
2022-01-07 23:41:24,257 botocore.hooks [DEBUG] Changing event name from request-created.machinelearning.Predict to request-created.machine-learning.Predict
2022-01-07 23:41:24,258 botocore.hooks [DEBUG] Changing event name from before-parameter-build.autoscaling.CreateLaunchConfiguration to before-parameter-build.auto-scaling.CreateLaunchConfiguration
2022-01-07 23:41:24,258 botocore.hooks [DEBUG] Changing event name from before-parameter-build.route53 to before-parameter-build.route-53
2022-01-07 23:41:24,258 botocore.hooks [DEBUG] Changing event name from request-created.cloudsearchdomain.Search to request-created.cloudsearch-domain.Search
2022-01-07 23:41:24,259 botocore.hooks [DEBUG] Changing event name from docs.*.autoscaling.CreateLaunchConfiguration.complete-section to docs.*.auto-scaling.CreateLaunchConfiguration.complete-section
2022-01-07 23:41:24,262 botocore.hooks [DEBUG] Changing event name from before-parameter-build.logs.CreateExportTask to before-parameter-build.cloudwatch-logs.CreateExportTask
2022-01-07 23:41:24,262 botocore.hooks [DEBUG] Changing event name from docs.*.logs.CreateExportTask.complete-section to docs.*.cloudwatch-logs.CreateExportTask.complete-section
2022-01-07 23:41:24,262 botocore.hooks [DEBUG] Changing event name from before-parameter-build.cloudsearchdomain.Search to before-parameter-build.cloudsearch-domain.Search
2022-01-07 23:41:24,263 botocore.hooks [DEBUG] Changing event name from docs.*.cloudsearchdomain.Search.complete-section to docs.*.cloudsearch-domain.Search.complete-section
2022-01-07 23:41:24,284 botocore.loaders [DEBUG] Loading JSON file: /home/dmedragh/.local/lib/python3.8/site-packages/botocore/data/endpoints.json
2022-01-07 23:41:24,292 botocore.hooks [DEBUG] Event choose-service-name: calling handler <function handle_service_name_alias at 0x7ff59754dd30>
2022-01-07 23:41:24,300 botocore.loaders [DEBUG] Loading JSON file: /home/dmedragh/.local/lib/python3.8/site-packages/botocore/data/polly/2016-06-10/service-2.json
2022-01-07 23:41:24,302 botocore.hooks [DEBUG] Event creating-client-class.polly: calling handler <function add_generate_presigned_url at 0x7ff5975fc820>
2022-01-07 23:41:24,304 botocore.endpoint [DEBUG] Setting polly timeout as (60, 60)
2022-01-07 23:41:24,306 botocore.loaders [DEBUG] Loading JSON file: /home/dmedragh/.local/lib/python3.8/site-packages/botocore/data/_retry.json
2022-01-07 23:41:24,306 botocore.client [DEBUG] Registering retry handlers for service: polly
2022-01-07 23:41:24,307 botocore.hooks [DEBUG] Event before-parameter-build.polly.SynthesizeSpeech: calling handler <function generate_idempotent_uuid at 0x7ff59757e1f0>
2022-01-07 23:41:24,307 botocore.hooks [DEBUG] Event before-call.polly.SynthesizeSpeech: calling handler <function inject_api_version_header_if_needed at 0x7ff59757fa60>
2022-01-07 23:41:24,307 botocore.endpoint [DEBUG] Making request for OperationModel(name=SynthesizeSpeech) with params: {'url_path': '/v1/speech', 'query_string': {}, 'method': 'POST', 'headers': {'Content-Type': 'application/json', 'User-Agent': 'Boto3/1.20.31 Python/3.8.5 Linux/5.4.72-microsoft-standard-WSL2 Botocore/1.23.31'}, 'body': b'{"Text": "I am David This is my first polly test", "OutputFormat": "mp3", "VoiceId": "Aditi"}', 'url': 'https://polly.us-east-1.amazonaws.com/v1/speech', 'context': {'client_region': 'us-east-1', 'client_config': <botocore.config.Config object at 0x7ff5973de610>, 'has_streaming_input': False, 'auth_type': None}}
2022-01-07 23:41:24,308 botocore.hooks [DEBUG] Event request-created.polly.SynthesizeSpeech: calling handler <bound method RequestSigner.handler of <botocore.signers.RequestSigner object at 0x7ff5973de4f0>>
2022-01-07 23:41:24,308 botocore.hooks [DEBUG] Event choose-signer.polly.SynthesizeSpeech: calling handler <function set_operation_specific_signer at 0x7ff59757e0d0>
2022-01-07 23:41:24,308 botocore.auth [DEBUG] Calculating signature using v4 auth.
2022-01-07 23:41:24,308 botocore.auth [DEBUG] CanonicalRequest:
POST
/v1/speech

content-type:application/json
host:polly.us-east-1.amazonaws.com
x-amz-date:20220107T224124Z

content-type;host;x-amz-date
43781c34dec677e80987fcef27cfe2c5f658a6c0c0e9e7d0f1b2935458f72caf
2022-01-07 23:41:24,309 botocore.auth [DEBUG] StringToSign:
AWS4-HMAC-SHA256
20220107T224124Z
20220107/us-east-1/polly/aws4_request
048106bf736952ae7348a7bfcf2601b887e10b511822a0a683d7710eba668557
2022-01-07 23:41:24,309 botocore.auth [DEBUG] Signature:
804c8094462fccaa0babd8f0fe86e256eba2b9f283728bebc2c7fe2800250375
2022-01-07 23:41:24,309 botocore.endpoint [DEBUG] Sending http request: <AWSPreparedRequest stream_output=True, method=POST, url=https://polly.us-east-1.amazonaws.com/v1/speech, headers={'Content-Type': b'application/json', 'User-Agent': b'Boto3/1.20.31 Python/3.8.5 Linux/5.4.72-microsoft-standard-WSL2 Botocore/1.23.31', 'X-Amz-Date': b'20220107T224124Z', 'Authorization': b'AWS4-HMAC-SHA256 Credential=AKIAWP3SBTKYBYO77FXH/20220107/us-east-1/polly/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature=804c8094462fccaa0babd8f0fe86e256eba2b9f283728bebc2c7fe2800250375', 'Content-Length': '93'}>
2022-01-07 23:41:24,310 botocore.httpsession [DEBUG] Certificate path: /etc/ssl/certs/ca-certificates.crt
2022-01-07 23:41:24,801 botocore.parsers [DEBUG] Response headers: {'x-amzn-RequestId': '98e092ed-0227-4689-a6b6-93f3d5497fd5', 'x-amzn-RequestCharacters': '38', 'Content-Type': 'audio/mpeg', 'Transfer-Encoding': 'chunked', 'Date': 'Fri, 07 Jan 2022 22:41:25 GMT'}
2022-01-07 23:41:24,802 botocore.parsers [DEBUG] Response body:
<botocore.response.StreamingBody object at 0x7ff5973b8940>
2022-01-07 23:41:24,802 botocore.hooks [DEBUG] Event needs-retry.polly.SynthesizeSpeech: calling handler <botocore.retryhandler.RetryHandler object at 0x7ff5973defa0>
2022-01-07 23:41:24,802 botocore.retryhandler [DEBUG] No retry needed.                                                         23:41:24 
 dmedragh@MSI      aws_Polly_sample  main  

### uplad lexicon 
``` aws polly put-lexicon --name awsLexicon --content file://aws-lexicon.xml ```

### Delete upladed lexicon 
``` aws polly delete-lexicon --name awsLexicon ```
