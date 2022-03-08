default:
	@echo ---- targets:
	@echo "   header.basic.local"
	@echo "   header.cors.local"
	@echo "   header.cors.s3"
	@echo "   "
	@echo "   content.range.cors.local"
	@echo "   content.range.cors.s3"
	@echo "   "
	@echo "   header.trena"
	@echo "   header.cors.trena"
	@echo "   ranged.content.cors.trena"
	@echo "   header.cors.trena.vcf"
	@echo "   ranged.content.cors.trena.vcf"
	@echo "   "
	@echo "   trenaTracks.html"


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

# -I header
# -L follow redirects
header.trena:
	curl -L -I http://igv-data.systemsbiology.net


header.cors.trena:
	curl -L -H "Access-Control-Request-Method: GET" \
              -H "Origin: http://hagfish.systemsbiology.net" \
              --head https://igv-data.systemsbiology.net/static/testFiles/nstd186.GRCh38.variant_call.vcf.gz

ranged.content.cors.trena:
	curl --range 0-999 -L -H "Access-Control-Request-Method: GET" \
              -H "Origin: http://hagfish.systemsbiology.net" \
              https://igv-data.systemsbiology.net/static/testFiles/nstd186.GRCh38.variant_call.vcf.gz \
              --output trena.cors.range.out
	@echo "    "
	@ls -l trena.cors.range.out

header.cors.trena.vcf:
	curl -L -H "Access-Control-Request-Method: GET" \
              -H "Origin: http://hagfish.systemsbiology.net" \
	--head "https://igv-data.systemsbiology.net/static/ampad/NIA-1898/chr22.vcf.gz"

ranged.content.cors.trena.vcf:
	curl --range 0-999 -L -H "Access-Control-Request-Method: GET" \
              -H "Origin: http://hagfish.systemsbiology.net" \
	"https://igv-data.systemsbiology.net/static/ampad/NIA-1898/chr22.vcf.gz" \
              --output trena.cors.range.vcf.out
	@echo "    "
	@ls -l trena.cors.range.vcf.out

trenaTracks-html:
	open trenaTracks.html





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

