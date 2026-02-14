PORTNAME=	spoofy
DISTVERSION=	v1.0.3.r0.g28db5fd
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Check if a list of domains can be spoofed based on SPF and DMARC records.
WWW=		https://github.com/MattKeeley/Spoofy

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-colorama@${PY_FLAVOR} \
		??/py-dnspython@${PY_FLAVOR} \
		??/py-openpyxl@${PY_FLAVOR} \
		??/py-pandas@${PY_FLAVOR} \
		??/py-tldextract@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
