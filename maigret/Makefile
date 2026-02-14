PORTNAME=	maigret
DISTVERSION=	main.r46.gb90cdb1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	OSINT username checker. Collect a dossier on a person by username from a huge number of sites.
WWW=		https://github.com/soxoj/maigret

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		devel/git \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/py-aiodns@${PY_FLAVOR} \
		??/py-aiohttp-socks@${PY_FLAVOR} \
		??/py-aiohttp@${PY_FLAVOR} \
		??/py-alive-progress@${PY_FLAVOR} \
		??/py-arabic-reshaper@${PY_FLAVOR} \
		??/py-async-timeout@${PY_FLAVOR} \
		??/py-attrs@${PY_FLAVOR} \
		??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-bidi@${PY_FLAVOR} \
		??/py-certifi@${PY_FLAVOR} \
		??/py-chardet@${PY_FLAVOR} \
		??/py-cloudscraper@${PY_FLAVOR} \
		??/py-colorama@${PY_FLAVOR} \
		??/py-dateutil@${PY_FLAVOR} \
		??/py-future-annotations@${PY_FLAVOR} \
		??/py-future@${PY_FLAVOR} \
		??/py-html5lib@${PY_FLAVOR} \
		??/py-idna@${PY_FLAVOR} \
		??/py-jinja@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-markupsafe@${PY_FLAVOR} \
		??/py-mock@${PY_FLAVOR} \
		??/py-multidict@${PY_FLAVOR} \
		??/py-networkx@${PY_FLAVOR} \
		??/py-pycountry@${PY_FLAVOR} \
		??/py-pypdf2@${PY_FLAVOR} \
		??/py-pysocks@${PY_FLAVOR} \
		??/py-requests-futures@${PY_FLAVOR} \
		??/py-socid-extractor@${PY_FLAVOR} \
		??/py-soupsieve@${PY_FLAVOR} \
		??/py-stem@${PY_FLAVOR} \
		??/py-tokenize-rt@${PY_FLAVOR} \
		??/py-torrequest@${PY_FLAVOR} \
		??/py-tqdm@${PY_FLAVOR} \
		??/py-typing_extensions@${PY_FLAVOR} \
		??/py-webencodings@${PY_FLAVOR} \
		??/py-xhtml2pdf@${PY_FLAVOR} \
		??/py-xmind@${PY_FLAVOR} \
		??/py-yarl@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
