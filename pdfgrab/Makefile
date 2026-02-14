PORTNAME=	pdfgrab
DISTVERSION=	15.1327508
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Tool for searching pdfs withthin google and extracting pdf metadata.
WWW=		https://github.com/c0decave/pdfgrab

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/ipython \
		??/py-google@${PY_FLAVOR} \
		??/py-json2html@${PY_FLAVOR} \
		??/py-pycryptodome@${PY_FLAVOR} \
		??/py-pypdf2@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
