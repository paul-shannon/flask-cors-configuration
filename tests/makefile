default:
	@echo ---- targets:
	@echo "   header.basic.local"
	@echo "   header.cors.local"
	@echo "   header.cors.s3"
	@echo "   content.range.cors.local"
	@echo "   content.range.cors.s3"

header.basic.local:
	curl -I http://localhost:60050

header.cors.local:
	curl -L -H "Access-Control-Request-Method: GET" \
              -H "Origin: http://bogus.systemsbiology.net" \
              --head http://localhost:60050

content.range.cors.local:
	curl --range 0-9 -L -H "Access-Control-Request-Method: GET" \
              -H "Origin: http://bogus.systemsbiology.net" \
              http://localhost:60050/static/date.txt.gz \
             --output local.cors.range.out
	@ls -l local.cors.range.out


# for comparison.  this apache server is provided by igv.js
header.cors.s3:
	curl -L -H "Access-Control-Request-Method: GET" \
              -H "Origin: http://hagfish.systemsbiology.net" \
              --head https://s3.amazonaws.com/igv.org.demo/nstd186.GRCh38.variant_call.vcf.gz

content.range.cors.s3:
	curl --range 0-99 -L -H "Access-Control-Request-Method: GET" \
              -H "Origin: http://hagfish.systemsbiology.net" \
              https://s3.amazonaws.com/igv.org.demo/nstd186.GRCh38.variant_call.vcf.gz \
             --output s3.cors.range.out
	@ls -l s3.cors.range.out


#
#
#ping:
#	curl -I https://igv-data.systemsbiology.net
#
#vcf.bug:
#	curl -O https://igv-data.systemsbiology.net/static/smallTestFiles/demo.narrowPeak.gz
#
#
#simple.range.request:
#	curl -I  --range 0-10 https://igv-data.systemsbiology.net/static/smallTestFiles/demo.narrowPeak.txt
#
#s3.header:
#	curl --range 0-99 -L -H "Access-Control-Request-Method: GET" \
#              -H "Origin: http://hagfish.systemsbiology.net" \
#              --head https://s3.amazonaws.com/igv.org.demo/nstd186.GRCh38.variant_call.vcf.gz
#s3.get:
#	curl --range 0-99 -L -H "Access-Control-Request-Method: GET" \
#              -H "Origin: http://hagfish.systemsbiology.net" \
#              https://s3.amazonaws.com/igv.org.demo/nstd186.GRCh38.variant_call.vcf.gz \
#              --output s3.get.out
#
#igv-data.header:
#	curl --range 0-99 -L -H "Access-Control-Request-Method: GET" \
#              -H "Origin: http://hagfish.systemsbiology.net" \
#              --head https://igv-data.systemsbiology.net/static/testFiles/nstd186.GRCh38.variant_call.vcf.gz
#
#igv-data.get:
#	curl --range 0-99 -L -H "Access-Control-Request-Method: GET" \
#              -H "Origin: http://hagfish.systemsbiology.net" \
#              https://igv-data.systemsbiology.net/static/testFiles/nstd186.GRCh38.variant_call.vcf.gz \
#             --output igv-data.get.out
#
#

