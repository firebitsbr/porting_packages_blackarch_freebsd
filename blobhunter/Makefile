PORTNAME=	blobhunter
DISTVERSION=	73.866a8c3
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Find exposed data in Azure with this public blob scanner.
WWW=		https://github.com/cyberark/BlobHunter

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-azure-common@${PY_FLAVOR} \
		??/py-azure-identity@${PY_FLAVOR} \
		??/py-azure-mgmt-core@${PY_FLAVOR} \
		??/py-azure-mgmt-resource@${PY_FLAVOR} \
		??/py-azure-mgmt-storage@${PY_FLAVOR} \
		??/py-azure-storage-blob@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
