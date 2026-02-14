PORTNAME=	python-textract
DISTVERSION=	1.6.5
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Extract text from any document. no muss. no fuss.
WWW=		https://pypi.org/project/textract/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/py-argcomplete@${PY_FLAVOR} \
		??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-chardet@${PY_FLAVOR} \
		??/py-docx2txt@${PY_FLAVOR} \
		??/py-ebooklib@${PY_FLAVOR} \
		??/py-pptx@${PY_FLAVOR} \
		??/py-speechrecognition@${PY_FLAVOR} \
		??/py-xlrd@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
